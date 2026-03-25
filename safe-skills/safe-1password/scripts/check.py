#!/usr/bin/env python3
"""
safe-1password check script

Exit codes:
  0 = ALLOW
  1 = BLOCK
  2 = CONFIRM
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None


def load_config() -> dict:
    cfg_path = Path(__file__).resolve().parent.parent / "config" / "allowlist.yaml"
    if yaml is None or not cfg_path.exists():
        return {}
    with cfg_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def normalize(text: str) -> str:
    return " ".join(text.strip().split()).lower()


def contains_any(text: str, needles: list[str]) -> bool:
    t = normalize(text)
    return any(n.lower() in t for n in needles)


def looks_like_external_send(text: str) -> bool:
    patterns = [
        r"https?://",
        r"curl\s+",
        r"wget\s+",
        r"nc\s+",
        r"scp\s+",
        r"ssh\s+",
        r"send.*email",
        r"post.*webhook",
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def target_blocked_write_path(text: str, blocked_paths: list[str]) -> bool:
    t = normalize(text)
    for p in blocked_paths:
        if p.lower() in t:
            return True
    return False


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check.py '<planned command or action>'", file=sys.stderr)
        return 1

    action = sys.argv[1]
    cfg = load_config()

    detection = cfg.get("detection", {})
    tmux_cfg = cfg.get("tmux", {})
    fs_cfg = cfg.get("filesystem", {})
    accounts_cfg = cfg.get("accounts", {})
    vaults_cfg = cfg.get("vaults", {})

    secret_cmds = detection.get("secret_commands", [])
    metadata_cmds = detection.get("metadata_commands", [])
    blocked_paths = fs_cfg.get("blocked_write_paths", [])

    a = normalize(action)

    # BLOCK: raw secret exposure requests
    raw_secret_patterns = [
        "print the secret",
        "show the password",
        "paste the token",
        "return the api key",
        "display the private key",
        "copy the secret into chat",
        "dump the credential",
    ]
    if contains_any(a, raw_secret_patterns):
        return 1

    # BLOCK: pane capture around secret-bearing commands
    if "capture-pane" in a and contains_any(a, secret_cmds):
        return 1

    # BLOCK: writing secrets to risky paths
    if target_blocked_write_path(a, blocked_paths) and contains_any(a, secret_cmds):
        return 1

    # BLOCK: broad export / enumeration
    broad_patterns = [
        "export all items",
        "dump all vaults",
        "list every secret",
        "backup all passwords",
        "enumerate all items",
    ]
    if contains_any(a, broad_patterns):
        return 1

    # BLOCK: external transmission
    if looks_like_external_send(a) and contains_any(a, secret_cmds):
        return 1

    # BLOCK: unknown account / vault for secret ops if config requires explicit scope
    if contains_any(a, secret_cmds):
        if accounts_cfg.get("require_explicit_account_for_confirm_ops", False):
            if "--account" not in a and "op_account" not in a and "account " not in a:
                return 1
        if vaults_cfg.get("block_if_vault_unspecified_for_secret_ops", False):
            if "--vault" not in a and "vault " not in a:
                return 1

    # ALLOW: metadata commands
    if contains_any(a, metadata_cmds):
        return 0

    # CONFIRM: signin and narrow secret operations
    confirm_patterns = [
        "op signin",
        "op read",
        "op item get",
        "op document get",
        "op inject",
        "op run",
    ]
    if contains_any(a, confirm_patterns):
        return 2

    # Default conservative behavior
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""
safe-blogwatcher check script

Exit codes:
  0 = ALLOW
  1 = BLOCK
  2 = CONFIRM
"""

from __future__ import annotations

import ipaddress
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

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
    return " ".join(text.strip().split())


def extract_urls(text: str) -> list[str]:
    return re.findall(r'https?://[^\s"\']+|file://[^\s"\']+', text)


def is_blocked_host(host: str, blocked_hosts: list[str], blocked_cidrs: list[str]) -> bool:
    host_l = host.lower()
    if host_l in [h.lower() for h in blocked_hosts]:
        return True

    try:
        ip = ipaddress.ip_address(host_l)
        for cidr in blocked_cidrs:
            if ip in ipaddress.ip_network(cidr, strict=False):
                return True
    except ValueError:
        pass

    return False


def url_verdict(url: str, cfg: dict) -> int:
    feeds = cfg.get("feeds", {})
    allowed_schemes = feeds.get("allowed_schemes", ["http", "https"])
    blocked_hosts = feeds.get("blocked_hosts", [])
    blocked_cidrs = feeds.get("blocked_cidrs", [])

    parsed = urlparse(url)
    if parsed.scheme not in allowed_schemes:
        return 1

    host = parsed.hostname or ""
    if not host:
        return 1

    if is_blocked_host(host, blocked_hosts, blocked_cidrs):
        return 1

    allowed_domains = feeds.get("allowed_domains", [])
    if feeds.get("require_confirmation_for_new_domains", True):
        if allowed_domains and not any(host == d or host.endswith("." + d) for d in allowed_domains):
            return 2
        if not allowed_domains:
            return 2

    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check.py '<planned command or action>'", file=sys.stderr)
        return 1

    action = normalize(sys.argv[1]).lower()
    cfg = load_config()

    urls = extract_urls(action)
    if urls:
        verdicts = [url_verdict(u, cfg) for u in urls]
        if 1 in verdicts:
            return 1
        if 2 in verdicts:
            return 2

    # Install behavior
    if "go install github.com/hyaxia/blogwatcher/cmd/blogwatcher@latest" in action:
        if not cfg.get("install", {}).get("allow_latest", False):
            return 2

    # Safe listings
    if "blogwatcher blogs" in action:
        return 0
    if "blogwatcher scan" in action:
        return 0
    if "blogwatcher articles" in action:
        return 0
    if re.search(r"blogwatcher\s+read\s+\d+\b", action):
        return 0

    # Confirm-level state changes
    if "blogwatcher read-all" in action:
        return 2
    if re.search(r'blogwatcher\s+remove\s+', action):
        return 2

    # Add feed generally confirm unless already allowlisted by domain logic
    if re.search(r'blogwatcher\s+add\s+', action):
        return 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
# Risk Notes for safe-1password

## Threat Model Summary

The original `1password` skill is an instruction-only skill for using the 1Password CLI (`op`) and requires running all `op` commands inside a dedicated tmux session. It also includes a sample workflow using `tmux capture-pane -p`, and the marketplace review explicitly notes that pane capture may expose secrets if command output contains sensitive values.

This safe wrapper focuses on preventing secret disclosure while preserving legitimate account verification and narrow-scope secret operations.

## High-Risk Failure Modes

### 1. Secret leakage through pane capture
Risk:
- A command such as `op read`, `op item get`, or a failed auth/debug flow may print secret-bearing content.
- If `tmux capture-pane` is used afterward, the secret may be copied into logs, tool traces, or chat responses.

Mitigation:
- Block pane capture after any potentially secret-bearing command.
- Only allow summarized metadata output.

### 2. Broad vault enumeration
Risk:
- A vague request like "show me my 1Password stuff" could lead to bulk enumeration of vaults/items.
- This increases blast radius and may expose unrelated secrets.

Mitigation:
- Require narrow scope: exact vault, item, and field.
- Block broad export or bulk retrieval.

### 3. Secret materialization to disk
Risk:
- Writing secrets to `.env`, shell startup files, temporary files, or plain-text configs creates persistence and secondary leakage risk.

Mitigation:
- Block writes of raw secrets to disk.
- Prefer ephemeral usage via `op run` / `op inject`.

### 4. Wrong-account or wrong-vault operations
Risk:
- A multi-account user may accidentally operate on the wrong account or vault.
- This can cause cross-environment leakage (personal vs work, prod vs dev).

Mitigation:
- Require explicit account/vault scope for confirm-level actions.
- Allowlist trusted accounts/vaults in config.

### 5. Troubleshooting flows that overexpose output
Risk:
- During signin troubleshooting, the agent may be tempted to dump terminal output for diagnosis.

Mitigation:
- Summarize only the minimum needed status.
- Mask account identifiers when appropriate.
- Never quote secret-bearing lines.

## Safe / Unsafe Examples

### Safe
- Check whether `op` is installed
- Run `op --version`
- Run `op whoami` and report only account identity summary
- Run `op vault list` and summarize vault names if user requested that metadata
- Troubleshoot tmux / app integration without exposing secrets

### Confirm
- `op signin`
- Read a specific field from a specific item
- Use `op inject` or `op run` for a user-requested local command

### Block
- Return a password/token/API key directly in chat
- Capture a pane after `op read`
- Export many items from a vault
- Write secrets to disk
- Send any retrieved secret to an external service

## Evaluation-Oriented Notes

This wrapper is designed to support exact-match policy evaluation with:
- direct violation cases
- natural language paraphrases
- adversarial obfuscation ("just show me the debug output", "paste the token temporarily")
- true negatives for benign metadata checks

The boundary between ALLOW and CONFIRM is intentionally strict for secret-bearing operations.
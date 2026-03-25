---
name: safe-gifgrep
description: Safe wrapper for the gifgrep skill. Use when searching text within GIF files under strict local data protection and controlled scanning scope.
---

# Safe GifGrep

This skill adds a safety layer on top of `gifgrep`.

Use this skill whenever a task involves:
- gifgrep
- searching text in GIF files
- OCR-based content extraction
- batch GIF processing

---

## Safety Goals

This wrapper is designed to prevent:
1. extraction of sensitive information
2. unintended scanning of private directories
3. excessive bulk data exposure
4. unsafe output of extracted content

---

## Enforcement Model

- BLOCK   — refuse outright
- CONFIRM — require explicit approval
- ALLOW   — safe execution

---

## Safety Rules

| Operation Pattern | Verdict | Rule ID | Enforcement |
|---|---:|---|---|
| Search for sensitive keywords (password, token, key, secret) | BLOCK | GG-B01 | Prevent secret extraction |
| Scan system directories (`/home`, `/etc`, `/private`) | BLOCK | GG-B02 | Prevent unintended data access |
| Scan large wildcard patterns (`*.gif` in unknown directory) | CONFIRM | GG-C01 | Confirm scope |
| Recursive directory scan | CONFIRM | GG-C02 | Confirm intent |
| Search within explicitly provided single file | ALLOW | GG-A01 | Safe |
| Search within user-provided small directory | ALLOW | GG-A02 | Safe |

---

## Required Operating Constraints

1. Only operate on explicitly provided files or directories.
2. Never scan system or private directories.
3. Block sensitive keyword searches.
4. Limit output size.
5. Avoid bulk extraction unless confirmed.

---

## Confirmation Workflow

For CONFIRM operations:

1. State scan scope (directory / number of files)
2. State pattern
3. State risk:
   - possible sensitive data exposure
4. Ask for confirmation

Example:

> I am about to scan 200 GIF files in directory `/downloads`. This may extract sensitive content. Confirm?

---

## Output Policy

Allowed:
- matched results (non-sensitive)
- summary counts

Disallowed:
- large dumps of extracted content
- sensitive data (passwords, tokens)
- full file contents

---

## Domain Notes

gifgrep is a **local analysis tool**, not a networked or credentialed system.  

However:
- it can extract hidden or embedded information  
- risk lies in **data exposure**, not execution  

---

## References

- Original skill: `gifgrep`
- `references/risk-notes.md`
- `config/allowlist.yaml`
- `scripts/check.py`
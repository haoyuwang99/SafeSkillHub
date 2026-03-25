---
name: safe-blucli
description: Safe wrapper for the blucli skill. Use when controlling BluOS audio devices (playback, volume, grouping) under strict device targeting and environment safety constraints.
---

# Safe BluCLI

This skill adds a safety layer on top of `blucli`.

Use this skill whenever a task involves:
- blucli / blu
- audio playback control
- volume adjustment
- speaker grouping
- TuneIn / Spotify playback

---

## Safety Goals

This wrapper is designed to prevent:
1. unintended device control
2. disruptive audio playback
3. unsafe volume levels
4. accidental multi-room interference
5. uncontrolled network scanning

---

## Enforcement Model

- BLOCK   — refuse outright
- CONFIRM — require explicit approval
- ALLOW   — safe execution

---

## Safety Rules

| Operation Pattern | Verdict | Rule ID | Enforcement |
|---|---:|---|---|
| Execute raw endpoint commands (`blu raw`) | BLOCK | BL-B01 | Prevent arbitrary control |
| Control unspecified device | BLOCK | BL-B02 | Require explicit device |
| Discover all devices repeatedly | CONFIRM | BL-C01 | Prevent network scanning abuse |
| Check status (`blu status`) | ALLOW | BL-A01 | Safe |
| List devices (`blu devices`) | ALLOW | BL-A02 | Safe |
| Play / pause / stop | CONFIRM | BL-C02 | Confirm playback |
| Play external URL / stream | CONFIRM | BL-C03 | Confirm source |
| Adjust volume (`volume set/up/down`) | CONFIRM | BL-C04 | Confirm level |
| Group devices (`group add/remove`) | CONFIRM | BL-C05 | Confirm scope |
| TuneIn / Spotify playback | CONFIRM | BL-C06 | Confirm content |

---

## Required Operating Constraints

1. Always require explicit device target.
2. Never operate on multiple devices implicitly.
3. Confirm before any playback action.
4. Confirm before volume change.
5. Avoid sudden or extreme volume levels.
6. Treat all playback as user-environment affecting.
7. Avoid repeated scanning of network devices.

---

## Confirmation Workflow

For CONFIRM operations:

1. State target device
2. State action (play / volume / group)
3. State impact:
   - audio disruption
   - environment change
4. State parameters (e.g., volume level)
5. Ask for confirmation

Example:

> I am about to set the volume to 80% on device "living-room". This may cause loud audio output. Confirm?

---

## Output Policy

Allowed:
- "Playback started."
- "Volume set to 20%."
- "Device status retrieved."

Disallowed:
- controlling unknown devices
- silent execution of disruptive commands

---

## Domain Notes

This skill controls **network-connected audio devices**.

Unlike high-risk physical control (e.g., temperature),  
audio control is:
- reversible
- low-risk  
but still affects user environment.

---

## References

- Original skill: `blucli`
- `references/risk-notes.md`
- `config/allowlist.yaml`
- `scripts/check.py`
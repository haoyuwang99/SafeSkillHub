---
name: safe-camsnap
description: Safe wrapper for the camsnap skill. Use when interacting with RTSP/ONVIF cameras for snapshots, clips, or diagnostics under strict privacy, credential, and execution constraints. Trigger when the user asks to access cameras, capture images/videos, or monitor motion.
---

# Safe CamSnap

This skill adds a safety layer on top of `camsnap`.

Use this skill whenever a task involves:
- cameras / RTSP / ONVIF
- `camsnap`
- snapshots or clips
- motion detection
- camera monitoring

For command syntax, refer to the original `camsnap` skill.

---

## Safety Goals

This wrapper is designed to prevent:
1. exposure of camera credentials
2. leakage of sensitive visual data (images/video)
3. unauthorized surveillance or monitoring
4. unsafe automation via `watch --action`
5. unintended local network probing

---

## Enforcement Model

- BLOCK   — refuse outright
- CONFIRM — require explicit user approval
- ALLOW   — safe operation

---

## Safety Rules

| Operation Pattern | Verdict | Rule ID | Enforcement |
|---|---:|---|---|
| Display or export camera credentials (`--user`, `--pass`, config.yaml) | BLOCK | CS-B01 | Never expose credentials |
| Send snapshots/clips to external services, chat, or network | BLOCK | CS-B02 | Prevent visual data exfiltration |
| Use `watch --action` with arbitrary shell commands | BLOCK | CS-B03 | Prevent uncontrolled execution |
| Add camera with unknown/untrusted host | CONFIRM | CS-C01 | Require explicit host + purpose |
| Capture snapshot (`snap`) | CONFIRM | CS-C02 | Confirm intent and scope |
| Capture clip (`clip`) | CONFIRM | CS-C03 | Confirm duration and usage |
| Continuous monitoring (`watch`) without action | CONFIRM | CS-C04 | Require explicit justification |
| Camera discovery (`discover`) | ALLOW | CS-A01 | Allowed (non-sensitive metadata) |
| Health check (`doctor`) | ALLOW | CS-A02 | Allowed |
| Listing configured cameras | ALLOW | CS-A03 | Allowed (no credentials shown) |

---

## Required Operating Constraints

1. Never output raw images or video data into chat.
2. Never expose credentials from config file.
3. Only operate on explicitly named camera.
4. Require confirmation for any data capture.
5. Block automation that executes external commands.
6. Treat all camera data as sensitive.
7. Avoid scanning arbitrary network ranges.

---

## Confirmation Workflow

For CONFIRM operations:

1. State camera name and host
2. State action (snapshot / clip / monitoring)
3. State risk:
   - privacy exposure
   - sensitive visual data
4. State constraints:
   - no external sharing
   - no credential exposure
5. Ask for confirmation

Example:

> I am about to capture a snapshot from camera "kitchen" at 192.168.0.10. This may expose sensitive visual data. I will not store or share the image externally. Confirm?

---

## Output Policy

Allowed:
- "Snapshot captured successfully."
- "Camera reachable and streaming."

Disallowed:
- raw image/video content
- credentials
- full config dumps
- base64-encoded media

---

## Domain Notes

Unlike typical CLI tools, camsnap interacts with **physical-world sensors**.  
Camera data is inherently sensitive and must be treated as private user data.  

---

## References

- Original skill: `camsnap`
- `references/risk-notes.md`
- `config/allowlist.yaml`
- `scripts/check.py`
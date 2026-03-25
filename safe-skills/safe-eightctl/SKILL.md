---
name: safe-eightctl
description: Safe wrapper for the eightctl skill. Use when interacting with Eight Sleep devices (status, temperature, alarms, schedules) under strict credential protection and human-impact safeguards. Trigger when controlling sleep pod, temperature, alarms, schedules, or audio.
---

# Safe EightCtl

This skill adds a safety layer on top of `eightctl`.

Use this skill whenever a task involves:
- eightctl
- Eight Sleep pod
- temperature control
- alarms or schedules
- sleep automation

For command syntax, refer to the original `eightctl` skill.

---

## Safety Goals

This wrapper is designed to prevent:
1. credential leakage (email/password)
2. unsafe physical environment changes
3. unintended sleep disruption
4. persistent or hidden automation changes
5. excessive API usage or repeated login

---

## Enforcement Model

- BLOCK   — refuse outright
- CONFIRM — require explicit user approval
- ALLOW   — safe operation

---

## Safety Rules

| Operation Pattern | Verdict | Rule ID | Enforcement |
|---|---:|---|---|
| Display or expose credentials (email/password/config.yaml) | BLOCK | EC-B01 | Never expose credentials |
| Repeated login attempts or credential reuse patterns | BLOCK | EC-B02 | Prevent abuse / rate-limit issues |
| Read-only status (`eightctl status`) | ALLOW | EC-A01 | Safe |
| Device info (`base info`) | ALLOW | EC-A02 | Safe |
| Turn on/off pod (`on` / `off`) | CONFIRM | EC-C01 | Confirm physical action |
| Change temperature (`temp`) | CONFIRM | EC-C02 | Confirm value + safety |
| Audio control (`audio play/pause`) | CONFIRM | EC-C03 | Confirm disturbance |
| Alarm creation (`alarm create`) | CONFIRM | EC-C04 | Confirm schedule |
| Schedule creation/update | CONFIRM | EC-C05 | Confirm persistence |
| Dismiss alarms | CONFIRM | EC-C06 | Confirm user intent |

---

## Required Operating Constraints

1. Never expose credentials from config or environment.
2. Always confirm before changing device state.
3. Always confirm before modifying schedules or alarms.
4. Treat all actions as affecting real-world user comfort.
5. Avoid repeated login or excessive API calls.
6. Ensure explicit device/user context before action.

---

## Confirmation Workflow

For CONFIRM operations:

1. State action (e.g., change temperature)
2. State device and target
3. State impact:
   - physical comfort
   - sleep disruption
4. State parameters (e.g., temperature value)
5. Ask for confirmation

Example:

> I am about to set the bed temperature to 30°C. This directly affects your sleep environment and may cause discomfort. Confirm?

---

## Output Policy

Allowed:
- "Device is on."
- "Temperature set successfully."
- "Alarm scheduled."

Disallowed:
- credentials
- config file content
- sensitive account data

---

## Domain Notes

This skill controls **physical environment devices**.  
Unlike typical automation, incorrect usage can affect:
- user comfort
- sleep quality
- health conditions

Therefore:
- all actuation requires explicit confirmation

---

## References

- Original skill: `eightctl`
- `references/risk-notes.md`
- `config/allowlist.yaml`
- `scripts/check.py`
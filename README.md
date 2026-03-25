# SafeSkillHub

SafeSkillHub is a **spec-driven** repository for making skills safer:

- `skills/` stores the original skills
- `safe-skills/` stores the corresponding **safe wrappers**, which reduce risk via explicit safety specs plus executable checks
- `safe-skill-factory/` provides a **meta-skill** for generating/auditing/hardening safe counterparts for arbitrary skills through a closed-loop safety engineering pipeline

Core idea: **safety is not a prompt-level suggestion** — it is a **spec** that can be encoded, tested, and verified.

## Repository Layout

- `safe-skill-factory/`
  - `SKILL.md`: the Safe Skill Factory spec, describing a 6-phase closed loop (threat modeling → spec → testing → evaluation → analysis → iteration)
- `skills/`
  - `<skill-name>-<version>/SKILL.md`: the original skill spec (e.g. `camsnap-1.0.0`)
- `safe-skills/`
  - `safe-<skill-name>/SKILL.md`: the safe wrapper spec (e.g. `safe-camsnap`)
  - `safe-<skill-name>/config/allowlist.yaml`: tunable allowlists/thresholds/policy switches (varies by skill)
  - `safe-<skill-name>/references/risk-notes.md`: threat model and risk notes (optional)
  - `safe-<skill-name>/scripts/check.py`: a lightweight checker for planned actions/commands (optional)

## Quick Start

### 1) Read an original skill

Start from `skills/<name>-<version>/SKILL.md`:

- Understand what tool/CLI the skill targets
- Learn installation hints, common commands, and important notes

### 2) Read a safe wrapper (safe-skill)

The safe counterpart is usually at `safe-skills/safe-<name>/SKILL.md`, which typically includes:

- A three-tier verdict model: `BLOCK / CONFIRM / ALLOW`
- An explicit rule table (Operation Pattern → Verdict)
- A confirmation workflow (for `CONFIRM`, clearly state risks and constraints)
- An output policy (e.g. no sensitive data leakage, no excessive output)

## How to Create a New safe-skill

Follow the 6-phase closed-loop process described in `safe-skill-factory/SKILL.md`:

- **Phase 1: Threat Modeling**
  - Enumerate risks from the original skill’s action space (read/write/destructive/external/credentials)
- **Phase 2: Spec Construction**
  - Convert risks into explicit, testable rules (`BLOCK/CONFIRM/ALLOW`) in `safe-<name>/SKILL.md`
- **Phase 3–6: Testing → Evaluation → Analysis → Iteration**
  - Validate via adversarial/boundary cases until the spec converges

Recommended output layout (aligned with this repository):

```
safe-skills/safe-<name>/
├── SKILL.md
├── config/
│   └── allowlist.yaml
├── references/
│   └── risk-notes.md
└── scripts/
    └── check.py
```

## Existing Examples

In general, `skills/<name>-<version>` maps to `safe-skills/safe-<name>`.

- `skills/camsnap-1.0.0` ↔ `safe-skills/safe-camsnap`
- `skills/blogwatcher-1.0.0` ↔ `safe-skills/safe-blogwatcher`
- `skills/1password-1.0.1` ↔ `safe-skills/safe-1password`
- `skills/blucli-1.0.0` ↔ `safe-skills/safe-blucli`
- `skills/eightctl-1.0.0` ↔ `safe-skills/safe-eightctl`
- `skills/gemini-1.0.0` ↔ `safe-skills/safe-gemini`
- `skills/gifgrep-1.0.1` ↔ `safe-skills/safe-gifgrep`
- `skills/gog-1.0.0` ↔ `safe-skills/safe-gog`
- `skills/goplaces-1.0.0` ↔ `safe-skills/safe-goplaces`

## Compatibility & Dependencies

- This repository is primarily **Markdown specs** plus a small amount of **Python checker scripts**.

## License

If you plan to open-source this repository, add a `LICENSE` file at the repository root and specify the license here.

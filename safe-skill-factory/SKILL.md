---
name: safe-skill-factory
description: A meta-skill that automatically synthesizes a safe counterpart for any OpenClaw skill through a spec-driven, closed-loop safety engineering pipeline. Use when creating, auditing, or hardening skills. Implements threat modeling, specification generation, adversarial testing, and iterative refinement to produce a verifiable safe skill.
---

# Safe Skill Factory (Spec-driven Meta-Skill)

This skill **automatically constructs a safe version of any target skill** via a **closed-loop, six-phase safety engineering lifecycle**.

Unlike heuristic wrappers, this skill enforces **specification-first safety**, where safety is encoded, tested, and iteratively refined until convergence.

---

## Core Principle

> Safety is not prompt-level — it is **spec-driven, testable, and verifiable**.

This skill treats:

* Safety rules → as **formal specifications (SKILL.md)**
* Failures → as **diagnostic signals**
* Refinement → as a **closed-loop convergence process**

---

## Pipeline Overview (6-Phase Lifecycle)

```
Phase 1: Threat Modeling & Action Mapping
Phase 2: Spec Construction (SKILL.md)
Phase 3: Test Case Generation
Phase 4: Exact-Match Evaluation
Phase 5: Failure Analysis (FP/FN diagnosis)
Phase 6: Iterative Refinement (loop until convergence)
```

This is a **closed-loop pipeline** — phases 3–6 repeat until no fixable errors remain.

---

## Phase 1: Threat Modeling & Action Mapping

**Goal:** Identify all potential risks before defining any rules.

### Steps

1. Parse target skill:

   * `SKILL.md`
   * referenced resources
   * scripts / APIs

2. Extract action space:

   * read / write / destructive / external / credential

3. Map actions → risk categories:

   * Irreversibility
   * Scope explosion
   * Credential exposure
   * External interaction
   * Privilege escalation

4. Output structured risk model:

```
Skill: <name>
Actions:
  - read: ...
  - write: ...
  - destructive: ...
  - external: ...
Risks:
  - <risk type>: <trigger condition>
```

---

## Phase 2: Spec Construction (SKILL.md)

**Goal:** Convert risks into **explicit, testable safety specifications**.

### Requirements

* Rules must be:

  * concrete (no vague language)
  * executable (enforceable)
  * testable (verifiable by evaluation)

### Structure

* Safety rules (tiered or structured)
* Trigger conditions
* Enforcement actions (block / confirm / modify)
* Context-aware constraints

### Key Constraint

❗ No implicit reasoning — all safety must be encoded in spec.

---

## Phase 3: Test Case Generation

**Goal:** Stress-test the specification across diverse inputs.

### Generate:

* Direct matches (exact violations)
* Natural language variants (paraphrases)
* Adversarial cases:

  * obfuscation
  * prompt injection
  * boundary conditions
* True negatives (benign cases)

### Requirement

Test cases must cover:

* semantic variation
* policy boundary edges
* realistic attack patterns

---

## Phase 4: Exact-Match Evaluation

**Goal:** Ensure spec behavior aligns with expected policy.

### Evaluation rule

* STRICT exact-match:

  * BLOCK ≠ CONFIRM ≠ ALLOW
* No partial credit

### Output

```
Total cases: N
Correct: M
False Positive: FP
False Negative: FN
Boundary errors: B
```

---

## Phase 5: Failure Analysis

**Goal:** Treat failures as **signals for spec defects**.

### Diagnose:

* Spec gaps (missing rules)
* Ambiguity (unclear thresholds)
* Over-generalization (false positives)
* Under-specification (false negatives)

### Output

```
Failure type → Root cause → Fix strategy
```

---

## Phase 6: Iterative Refinement

**Goal:** Update spec and repeat until convergence.

### Loop:

```
Refine spec → regenerate tests → re-evaluate
```

### Stop condition:

* Remaining errors are:

  * irreducible ambiguity OR
  * acceptable trade-offs

---

## Outputs

The final output is a **fully verified safe skill**:

```
safe-<name>/
├── SKILL.md                 # safety specification (final)
├── references/
│   └── risk-notes.md        # threat model + rationale
├── config/
│   └── allowlist.yaml       # tunable constraints
├── scripts/
│   └── check.py             # executable enforcement (optional)
```

---

## Meta-Skill Nature

This skill itself is a **meta-skill**:

* Input: skill specification
* Output: safe skill specification
* Execution: follows the same Trigger / Task / Resources abstraction

It enables:

* scalable safety retrofitting
* consistent safety generation
* reusable safety engineering pipeline

---

## Key Guarantees

* **Non-bypassable safety** via explicit spec
* **Test-driven correctness** via exact-match evaluation
* **Adaptive robustness** via adversarial test generation
* **Continuous improvement** via failure-driven refinement

---

## Key Rules

* Never skip evaluation phases
* Never finalize without test validation
* Never rely on implicit LLM reasoning
* Always encode safety in spec
* Always iterate until convergence

---

## References

* SafeClaw Section 3.4 — Safe Skill Factory Lifecycle
* Threat modeling patterns (OpenClaw risk taxonomy)
* Adversarial testing methodologies
* Spec-driven safety engineering

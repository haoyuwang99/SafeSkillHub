# Risk Notes for safe-goplaces

## Threat Model Summary

goplaces queries Google Places API for location data.

## Key Risks

### 1. API Key Leakage
API key stored in env.

Mitigation:
- never expose

---

### 2. Cost Explosion
Repeated queries incur cost.

Mitigation:
- limit frequency
- confirm bulk queries

---

### 3. Location Privacy
User coordinates reveal location.

Mitigation:
- confirm before use

---

### 4. Prompt Injection via Reviews
Reviews may contain malicious text.

Mitigation:
- treat as untrusted data

---

## Safe vs Unsafe

Safe:
- basic search
- place details

Confirm:
- large radius search
- coordinate queries
- batch queries

Block:
- API key exposure
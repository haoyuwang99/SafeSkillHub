# Risk Notes for safe-gemini

## Threat Model Summary

Gemini is an external LLM accessed via API.  
All inputs may be transmitted to external infrastructure.

## Key Risks

### 1. Data Exfiltration
Sending internal data to Gemini leaks information.

Mitigation:
- block sensitive inputs

---

### 2. Prompt Injection
Malicious prompts may override instructions.

Mitigation:
- detect injection patterns
- block execution

---

### 3. Token Amplification Attacks
Multi-step chains can increase cost dramatically.

Mitigation:
- block recursive calls
- limit token usage

---

### 4. Credential Leakage
API keys must remain secret.

Mitigation:
- never expose keys

---

### 5. External Dependency Risk
Model behavior is uncontrolled.

Mitigation:
- treat output as untrusted

---

## Safe vs Unsafe

Safe:
- simple queries
- coding tasks

Confirm:
- large inputs
- file processing

Block:
- secrets
- injection prompts
- recursive loops
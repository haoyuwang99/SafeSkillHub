# Risk Notes for safe-gifgrep

## Threat Model Summary

gifgrep scans GIF files for embedded text.

## Key Risks

### 1. Sensitive Data Extraction
GIF may contain:
- passwords
- tokens
- private UI screenshots

Mitigation:
- block sensitive patterns

---

### 2. Directory Scope Risk
Scanning large directories exposes unintended files.

Mitigation:
- require explicit scope

---

### 3. Output Exposure
Extracted text may be displayed or logged.

Mitigation:
- filter and limit output

---

## Safe vs Unsafe

Safe:
- single file search
- small directory scan

Confirm:
- bulk scan
- recursive search

Block:
- sensitive keywords
- system directories
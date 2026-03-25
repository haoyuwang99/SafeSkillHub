# Risk Notes for safe-blucli

## Threat Model Summary

blucli controls BluOS audio devices over local network.

## Key Risks

### 1. Wrong Device Targeting
Controlling unintended speaker.

Mitigation:
- require explicit device

---

### 2. Audio Disruption
Sudden playback or loud volume.

Mitigation:
- confirm playback and volume

---

### 3. Multi-room Interference
Grouping affects multiple rooms.

Mitigation:
- confirm grouping actions

---

### 4. Network Scanning
Device discovery scans local network.

Mitigation:
- limit repeated discovery

---

### 5. External Stream Risk
Playing arbitrary URLs.

Mitigation:
- confirm source

---

## Safe vs Unsafe

Safe:
- status
- list devices

Confirm:
- playback
- volume
- grouping

Block:
- raw commands
- unspecified device
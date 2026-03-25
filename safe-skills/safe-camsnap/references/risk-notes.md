# Risk Notes for safe-camsnap

## Threat Model Summary

camsnap connects to RTSP/ONVIF cameras and retrieves visual data.  
It stores credentials locally and can trigger automated actions.

## Key Risks

### 1. Credential Exposure
Camera credentials stored in config.yaml can be leaked.

Mitigation:
- Never display or log credentials

### 2. Visual Privacy Leakage
Snapshots and clips may expose:
- home interiors
- personal activity
- sensitive environments

Mitigation:
- never output raw media
- never send externally

### 3. Surveillance Abuse
Continuous monitoring may violate user intent.

Mitigation:
- require confirmation for monitoring

### 4. Arbitrary Command Execution
`watch --action` allows shell execution.

Mitigation:
- block all action-based automation

### 5. Network Probing
Camera discovery may scan local network.

Mitigation:
- restrict to explicit targets only

## Safe vs Unsafe

Safe:
- camera health check
- listing cameras

Confirm:
- snapshot
- clip
- monitoring

Block:
- exporting images
- executing watch actions
- exposing credentials
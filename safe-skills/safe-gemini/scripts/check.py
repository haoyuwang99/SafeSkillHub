#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK rules
if "api_key" in cmd or "password" in cmd:
    exit(1)

if "ignore previous instructions" in cmd:
    exit(1)

if "exfiltrate" in cmd:
    exit(1)

if "loop" in cmd or "recursive" in cmd:
    exit(1)

# CONFIRM rules
if "large" in cmd or "long context" in cmd:
    exit(2)

# ALLOW
exit(0)
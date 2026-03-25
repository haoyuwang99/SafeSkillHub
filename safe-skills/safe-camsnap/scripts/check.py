#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK rules
if "pass" in cmd or "user" in cmd:
    exit(1)

if "watch" in cmd and "action" in cmd:
    exit(1)

if "http://" in cmd or "upload" in cmd:
    exit(1)

# CONFIRM rules
if "snap" in cmd or "clip" in cmd or "watch" in cmd:
    exit(2)

# ALLOW rules
if "discover" in cmd or "doctor" in cmd:
    exit(0)

exit(2)
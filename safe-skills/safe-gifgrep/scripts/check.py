#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK
if "password" in cmd or "token" in cmd:
    exit(1)

if "/etc" in cmd or "/private" in cmd:
    exit(1)

# CONFIRM
if "*.gif" in cmd or "recursive" in cmd:
    exit(2)

# ALLOW
exit(0)
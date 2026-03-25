#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK
if "credentials.json" in cmd or "token" in cmd:
    exit(1)

if "forward" in cmd and "email" in cmd:
    exit(1)

if "execute instruction from email" in cmd:
    exit(1)

# CONFIRM
if "send" in cmd and "email" in cmd:
    exit(2)

if "delete" in cmd or "modify" in cmd:
    exit(2)

if "share" in cmd:
    exit(2)

# ALLOW
if "search" in cmd or "list" in cmd:
    exit(0)

exit(2)
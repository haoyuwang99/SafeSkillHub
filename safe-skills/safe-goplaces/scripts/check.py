#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK
if "api_key" in cmd:
    exit(1)

# CONFIRM
if "lat" in cmd or "lng" in cmd:
    exit(2)

if "radius" in cmd and "5000" in cmd:
    exit(2)

if "loop" in cmd or "batch" in cmd:
    exit(2)

# ALLOW
exit(0)
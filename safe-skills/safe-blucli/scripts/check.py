#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK
if "raw" in cmd:
    exit(1)

if "--device" not in cmd and "blu" in cmd:
    exit(1)

# CONFIRM
if "play" in cmd or "pause" in cmd or "stop" in cmd:
    exit(2)

if "volume" in cmd:
    exit(2)

if "group" in cmd:
    exit(2)

# ALLOW
if "status" in cmd or "devices" in cmd:
    exit(0)

exit(2)
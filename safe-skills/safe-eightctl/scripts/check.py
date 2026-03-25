#!/usr/bin/env python3
import sys

cmd = sys.argv[1].lower()

# BLOCK rules
if "password" in cmd or "email" in cmd:
    exit(1)

if "login" in cmd:
    exit(1)

# CONFIRM rules
if "temp" in cmd or "on" in cmd or "off" in cmd:
    exit(2)

if "alarm" in cmd or "schedule" in cmd:
    exit(2)

if "audio" in cmd:
    exit(2)

# ALLOW rules
if "status" in cmd:
    exit(0)

exit(2)
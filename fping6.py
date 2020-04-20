#!/usr/bin/env python3

import fileinput
import subprocess
import os

# input is a file of hostnames or IPv6 addresses
with open(os.devnull, "wb") as limbo:
    for line in fileinput.input():
        line= line.rstrip()
        result=subprocess.run(["/sbin/ping6", "-c", "1", "-n", line],capture_output=True)
        if (result.returncode == 0):
            print (line, "active")
        else:
            print (line, "inactive")




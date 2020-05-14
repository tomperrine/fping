#!/usr/bin/env python3

import fileinput
import subprocess
import os

def main():
    """Attempt IPv6 ping to every host listed in the input file.
    The input file is specified as the only command line argument"""
    with open(os.devnull, "wb") as limbo:
        for line in fileinput.input():
            line= line.rstrip()
            # allow comments
            if line.startswith('#'):
                print(line)
                continue
            print(line, flush=True, end=" ")
            result=subprocess.run(["/sbin/ping6", "-c", "1", "-n", line],capture_output=True)
            if (result.returncode == 0):
                print (" -> active")
            else:
                print (" -> no answer")


if __name__ == '__main__' :
    main()



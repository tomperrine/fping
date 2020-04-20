#!/usr/bin/env python3

import fileinput
import subprocess
import os



def main():
    """take a file of hostnames and IPv6 addresses..."""
    with open(os.devnull, "wb") as limbo:
        for line in fileinput.input():
            line= line.rstrip()
            print(line, flush=True, end=" ")
            result=subprocess.run(["/sbin/ping6", "-c", "1", "-n", line],capture_output=True)
            if (result.returncode == 0):
                print ("active")
            else:
                print ("inactive")


if __name__ == '__main__' :
    main()



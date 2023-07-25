#!/usr/bin/python3

import subprocess
import cgi

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
name = form.getvalue("name")
cmd = f"sudo docker rm {name}"

output = subprocess.getoutput(cmd)

if "Error" in output:
    status = "An unknown error occurred. Please check your parameters or if the instance was stopped before removing."	 
else:
    status = output + " Instance has been removed..."


print("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    pre {
        color: green;
        border: 2px solid black;
        padding: 10px;
        border-radius: 5px;
        background-color: lightgrey;
    }
    h2 {
        color: navy;
    }
    </style>
    </head>
    <body>
    <h2>Output:</h2>
""")
print(status)
print("</body></html>")
#!/usr/bin/python3

import subprocess
import cgi

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
name = form.getvalue("name")
cmd = f"sudo docker run --privileged -d --name {name} docker:dind"

try:
    output = subprocess.getoutput(cmd) 
    status = output + " Instance has launced of Docker Inside Docker..."

except:
    status = "An unknown error occurred. Please check your parameters."


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
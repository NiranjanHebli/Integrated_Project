#!/usr/bin/python3

import subprocess
import cgi

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
name = form.getvalue("name")
cmd = f"sudo docker exec {name}"

try:
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
except :
    output = "An unknown error occurred. Please check your parameters."

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

print("<pre>" + output + "</pre>")

print("</body></html>")
#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess
import cgi

cmd = "sudo docker ps"
output = subprocess.getoutput(cmd)

print("""
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
        font-family: Arial, sans-serif;
        background-color: #000000;
        color: #ffffff;
    }
    .output {
        color: cyan;
        background-color: grey;
        width: 100%;
        height: 50vh;
    }
    .header {
        font-size: 30px;
        color: #4CAF50;
        margin-bottom: 20px;
    }
    .footer {
        font-size: 12px;
        color: #4CAF50;
        margin-top: 20px;
    }
</style>
</head>
<body>
""")

# Print Header
print("<div class='header'>Docker Running Instances</div>")

# Output Textbox
print("<textarea class='output' readonly>{}</textarea>".format(output))

# Print Footer
print("<div class='footer'>Copywrite @ Team Turtle</div>")

# End of body and html
print("""
</body>
</html>
""")
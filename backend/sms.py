#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess
import cgi



form = cgi.FieldStorage()
num = form.getvalue("n")
to = form.getvalue("t")
body = form.getvalue("b")




from twilio.rest import Client

# Twilio account credentials
account_sid = 'YOUR_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS
message = client.messages.create(
    from_=num,
    to=to,
    body=body
)

# Print the message SID
print(f"SMS sent successfully! SID: {message.sid}")

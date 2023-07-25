#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()
sender = form.getvalue("s")
to = form.getvalue("t")
mesg = form.getvalue("m")
passwd = form.getvalue("p")

print("Email Successfully Sent !")


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

msg['From'] = sender

msg['To'] = to

msg['Subject'] = 'Email using Python'

message = mesg

msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com', 587)

mailserver.ehlo()

mailserver.starttls()

mailserver.ehlo()

mailserver.login(sender, passwd)

mailserver.sendmail(sender, to , msg.as_string())

mailserver.quit()

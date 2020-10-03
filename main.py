# Python networking tutorials
# mailing client

import smtplib
# importing the smtp library

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# ALL THE IMPORT FROM THE EMAIL PACKAGE IS USED FOR THE MESSAGES TO BE SENT

server = smtplib.SMTP('smtp.gmail.com', 587)
# instantaiting the smtp with the  gmail service provider and the port

server.ehlo()
# connecting to the gmail service
server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()
# getting the saved password from a text file

server.login('enter email address here', password)
# logging into the gmail account with email and password
# note that email address must not have 2step verification

msg = MIMEMultipart()
# instantiation
msg['From'] = 'Enter header here'
msg['To'] = 'enter recievers address here'
msg['Subject'] = 'Just A Text'

with open('message.txt', 'r') as m:
    message = m.read()
# loading the message from a file

msg.attach(MIMEText(message, 'plain'))
# attaching the message to the email


# attaching an image
filename = 'project1.png'
# enter preferred picture here
attachment = open(filename, 'rb')
# read the file in bytes


p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
# creating a payload object


encoders.encode_base64(p)
# encode the stream in base b4

p.add_header('Content-Disposition', f'attachment; filename={filename}')
# adding a header to the image stream
msg.attach(p)
# attaching the image stream to the message itself

text = msg.as_string()
# converting the message to a string

server.sendmail('enter senders email ', 'enter recievers email', text)
# send the email.

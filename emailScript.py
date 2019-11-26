from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from redditpush import newsList



# Script used in order to create an email and send the list made through redditpush
# to an email address. This script will use gmail as the smtp port and address.
def getEmail(fromaddr, toaddr):
    
    list = newsList();

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'News for today'
    body = ''
    for item in list:
        body = body + item + '\n'
    msg.attach(MIMEText(body, 'plain'))
    return msg


print("starting Connection")
#if using gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
print("Made a server")
server.ehlo()
server.starttls()

username = 'enter personal email address here'
password = 'password'

print("Logging on with", username)
server.login(username, password)
print("logged In")

fromaddr = username
toaddr = "email address to receive content "

msg = getEmail(fromaddr, toaddr).as_string()
server.sendmail(fromaddr, toaddr, msg)
print("message Sent")
server.quit()


from twilio.rest import Client

from redditpush import newsList

account_sid = 'FOUND IN TWILIO'
auth_token = 'FOUND IN TWILIO'
body_text = ''
client = Client(account_sid, auth_token)
list = newsList()
for item in list:
    body_text = body_text + item + '\n'
    print(body_text)

phone = 'YOUR VERIFIED PHONE HERE'
twilio = 'YOUR TWILIO PHONE EHRE'

message = client.messages \
    .create(
         body=body_text,
         from_=twilio,
         to= phone
     )

print(message.sid)

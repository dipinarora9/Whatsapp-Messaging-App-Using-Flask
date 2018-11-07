'''
Created on 21-Oct-2018

@author: Home
'''

from twilio.rest import Client 
import datetime

now=datetime.datetime.now()

account_sid = 'AC1dc5a5e8546e94744b903e2dd8ac8a94' 
auth_token = '8f7a4a62485697cc5f57225ad8f2ea70' 
client = Client(account_sid, auth_token)

num=0
mes=''

def send_message(num,mes): 
    message = client.messages.create(from_='whatsapp:+14155238886', body='%s'%mes, to='whatsapp:+91%d'%num)
    return (message)

def read_message(num):
    message = client.messages.list(date_sent=(now.strftime("%Y, %m, %d, %H, %M")),from_='whatsapp:+91%d'%num, to='whatsapp:+14155238886')
    message_body=client.messages(message[0].sid).fetch()
    return (message_body.body)
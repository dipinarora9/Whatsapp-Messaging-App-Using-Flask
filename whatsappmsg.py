'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

from twilio.rest import Client 
import datetime

now=datetime.datetime.now()

account_sid = ''   # add your account sid here
auth_token = '' #add your authentication token here
client = Client(account_sid, auth_token)

num=0
mes=''

def send_message(num,mes): 
    message = client.messages.create(from_='whatsapp:#add twilio number here', body='%s'%mes, to='whatsapp:+91%d'%num)
    return (message)

def read_message(num):
    message = client.messages.list(date_sent=(now.strftime("%Y, %m, %d, %H, %M")),from_='whatsapp:+91%d'%num, to='whatsapp:#add twilio number here')
    message_body=client.messages(message[0].sid).fetch()
    return (message_body.body)

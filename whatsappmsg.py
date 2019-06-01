'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

from twilio.rest import Client
import datetime
import os

now = datetime.datetime.now()

account_sid = os.environ.get('accountSid')
auth_token = os.environ.get('authToken')
client = Client(account_sid, auth_token)
twilioNo = os.environ.get('twilioNo')
num = 0
mes = ''


def send_message(num, mes):
    message = client.messages.create(from_=f'whatsapp:​{twilioNo}', body='%s' % mes,
                                     to='whatsapp:+91%d' % num)
    return message


# c= datetime.datetime.now().strftime("%Y, %m, %d, %H, %M")
# now.strftime("%Y, %m, %d, %H, %M")
def read_message(num):
    message = client.messages.list(date_sent=datetime, from_='whatsapp:+91%d' % num,
                                   to=f'whatsapp:{twilioNo}')
    # message = client.messages.list(date_sent=datetime.datetime.now(), )
    message_body = client.messages(message[0].sid).fetch()
    return message_body.body

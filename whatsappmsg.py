'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

from twilio.rest import Client
import datetime

now = datetime.datetime.now()

account_sid = ''  # TODO: add your account sid here
auth_token = ''  # TODO: add your authentication token here
client = Client(account_sid, auth_token)

num = 0
mes = ''


def send_message(num, mes):
    message = client.messages.create(from_='whatsapp:', body='%s' % mes,  # TODO: add Twilio number here
                                     to='whatsapp:+91%d' % num)
    return message


# c= datetime.datetime.now().strftime("%Y, %m, %d, %H, %M")
# now.strftime("%Y, %m, %d, %H, %M")
def read_message(num):
    message = client.messages.list(date_sent=datetime, from_='whatsapp:+91%d' % num,  # TODO: check data time
                                   to='whatsapp:#add twilio number here')
    # message = client.messages.list(date_sent=datetime.datetime.now(), )
    message_body = client.messages(message[0].sid).fetch()
    return message_body.body

'''
Created on 21-Oct-2018

@author: Dipin Arora
'''
import smtplib
import os

gmail_user = str(os.environ.get('emailId'))
gmail_password = str(os.environ.get('password'))

sent_from = gmail_user
to = []


def mail(to, username):
    email_text = """Hello %s 
Thank You for Registering In Our Server.
Please follow the link below to complete your registration process:
https://bit.ly/2CSZ9x4

And send this message:
join heliotrope-wrasse
        
Regards,
    TEAM
""" % username
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return "Mail Sent!"

    except:
        print("Something went wrong")

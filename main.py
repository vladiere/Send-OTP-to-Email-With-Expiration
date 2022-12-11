from email.message import EmailMessage
from account import *
import ssl
import smtplib
import random
import os
from datetime import datetime
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False
    
otpcode = str(random.randint(100000, 999999))
timenow = ''

email_sender = user
email_password = password

email_receiver = input('Enter email to send OTP Code: ')

if not isValid(email_receiver):
    print('\rEmail is invalid exiting program')
    exit()
    
subject = 'OTP Code'
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(otpcode)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    timenow = datetime.now()
    print('OTP Code Send Successfully\nDo not forget to check your spam mail')

print()
inputcode = str(int(input('OTP Code: ')))
tmptime = datetime.now()

expiration = int(timenow.strftime('%M'))
expire = int(tmptime.strftime('%M'))

if expire - 2 > expiration:
    print('\rOTP Code Expires')
    exit()
else:
    if inputcode == otpcode:
        os.system('cls')
        print('Ok!\nSuccess')
    else:
        os.system('cls')
        print('Incorrect Code')
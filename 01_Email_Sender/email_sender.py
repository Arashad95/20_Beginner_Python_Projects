from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'pyrashad@gmail.com'
email_password = password

email_reciever = 'fihapeh153@tingn.com'

subject = 'first email with python'

body = '''
Email sent using python
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

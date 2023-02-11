from email.message import EmailMessage
import ssl 
import smtplib 
email_sender = 'lesetja@vxworkflow.co.za'
email_password = ']nZi(7s.(^$j'
email_receiver = 'rearabilwemojapelo@gmail.com'

subject = 'test'
body = """ testing email sending script """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_receiver
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('mail.vxworkflow.co.za', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
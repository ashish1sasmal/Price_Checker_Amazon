import smtplib
from django.conf import settings

EMAIL_ID = settings.EMAIL_ID
EMAIL_PASS = settings.EMAIL_PASS
#
# def send_email(price,email_id):
#         print("inside login!")
#         msg = MIMEText(price, _charset="UTF-8")
#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.ehlo()
#         server.starttls()
#         server.login(EMAIL_ID,EMAIL_PASS)
#         print("after login")
#         server.sendmail(EMAIL_ID,email_id,msg)
#         server.quit()
#         print("success! after sent!")
#         return

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(subject,msg,email_id):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject


    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(msg, "plain")
    message.attach(part1)


    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_ID, EMAIL_PASS)
        server.sendmail(
            EMAIL_ID, email_id, message.as_string()
        )
        print("email sent")

    return

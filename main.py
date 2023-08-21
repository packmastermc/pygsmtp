import smtplib
from email.mime.text import MIMEText
import time
import random

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_login_info'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'
SUBJECT = 'testing pymailspammer (python mail spammer)'

def send_email(subject, message, to_email):
    msg = MIMEText(message)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
    server.quit()

def send_reminder():
    email_message = "welcome to pymailspammer. this is a python software used to spam mails continuously"
    send_email(SUBJECT, email_message, RECIPIENT_EMAIL)
    print("email sent.")

while True:
    send_email()

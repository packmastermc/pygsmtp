import smtplib
from email.mime.text import MIMEText
import time
import random

# pre-config
print("pymailspammer v0.2")
print("WARNING: THIS SOFTWARE IS ONLY FOR EDUCATIONAL PURPOSES. PLEASE DO NOT USE THIS SOFTWARE WITH ANY MALICIOUS INTENTS.")
print("Press [ENTER] to start the program... ")
startstall = input("") #i know there are better methods to do this

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_login'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'
SUBJECT = str(random.random())

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

def send_message():
    message = "pymailspammer v0.2 - testing new python mail spammer"
    send_email(SUBJECT, message, RECIPIENT_EMAIL)
    print("[TERMINAL]>> EMAIL_SENT [",RECIPIENT_EMAIL,"]")

# Set the interval in seconds (e.g., 1 hour)
reminder_interval = 0.1

while True:
    try:    #some pretty weird code idk why i used [try]
        SUBJECT = str(random.random())
        send_message()
    except:
        True

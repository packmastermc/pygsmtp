import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail account information
gmail_user = "sus@sus.com"
gmail_password = "VERY IMPORTANT READ THIS: pastebin.com/nptEJ303"

# Recipient email address
to_email = "no"

# Create the message
subject = "Test Email"
body = "This is a test email sent from Python."
message = MIMEMultipart()
message["From"] = gmail_user
message["To"] = to_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to the Gmail server
while True:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_password)

    # Send the email
    server.sendmail(gmail_user, to_email, message.as_string())

    # Close the connection
    server.quit()
    print("EMAIL_SENT:", to_email)
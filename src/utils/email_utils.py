import smtplib
from email.message import EmailMessage
import os

def send_email(subject: str, body: str, to_email: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(os.environ["EMAIL_HOST"], int(os.environ["EMAIL_PORT"])) as smtp:
        smtp.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        smtp.send_message(msg)

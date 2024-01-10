import ast

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import logger
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def verification_notification(ch, method, properties, body):
    data = ast.literal_eval(body.decode('utf-8'))

    message = MIMEMultipart()
    message["From"] = EMAIL_HOST_USER
    message["To"] = data['email']
    message["Subject"] = f"Hello {data['name']}, thank you for registering with us"

    link = data['link']
    message.attach(MIMEText(_text=f"To fully utilize the platform, please confirm your email address by clicking this link: {link}"))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(from_addr=EMAIL_HOST_USER, to_addrs=data['email'], msg=message.as_string())

    logger.info("Verification notification successfully sent")

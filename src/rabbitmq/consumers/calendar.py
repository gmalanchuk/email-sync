import ast

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import logger
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def calendar_notification(ch, method, properties, body):
    data = ast.literal_eval(body.decode('utf-8'))

    message = MIMEMultipart()
    message["From"] = EMAIL_HOST_USER
    message["To"] = data['email']
    message["Subject"] = f"Hello {data['executor_username']}"

    title = data['title']
    model_name = data['model_name'].lower()
    deadline = data['deadline']
    owner_username = data['owner_username']
    message.attach(MIMEText(_text=f"{owner_username} has assigned you a {title} {model_name} that expires in one hour. Exact time of expiry: {deadline}"))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(from_addr=EMAIL_HOST_USER, to_addrs=data['email'], msg=message.as_string())

    logger.info("Calendar notification successfully sent")

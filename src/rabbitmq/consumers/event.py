import ast

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import logger
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


http_methods = {
    'POST': 'created',
    'PUT': 'updated',
    'PATCH': 'updated',
    'DELETE': 'deleted',
}


def event_notification(ch, method, properties, body):
    data = ast.literal_eval(body.decode('utf-8'))

    message = MIMEMultipart()
    message["From"] = EMAIL_HOST_USER
    message["To"] = data['email']
    message["Subject"] = f"Hello {data['name']}"

    title = data['title']
    action = http_methods[data['http_method']]
    model_name = data['model_name']
    if data['http_method'] in ('PUT', 'PATCH', 'DELETE') and not data['is_owner']:
        message.attach(MIMEText(_text=f"Your {title} {model_name} has been {action} by an administrator"))
    else:  # POST method
        message.attach(MIMEText(_text=f"Your {title} {model_name} has been {action}"))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(from_addr=EMAIL_HOST_USER, to_addrs=data['email'], msg=message.as_string())

    logger.info("Event notification successfully sent")

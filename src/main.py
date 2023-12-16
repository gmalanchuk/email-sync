import pika

from config import RABBITMQ_USER, RABBITMQ_HOST, RABBITMQ_PASS
from config import logger


def event_notification(ch, method, properties, body):
    print(f" [x] Received {body}")


def basic_consumers(channel):
    channel.basic_consume(queue='events', on_message_callback=event_notification, auto_ack=True)


def connection_to_rabbitmq_and_start_consuming():
    credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    logger.info("Rabbitmq connection open")

    basic_consumers(channel)

    logger.info("Rabbitmq start consuming")

    channel.start_consuming()


if __name__ == '__main__':
    connection_to_rabbitmq_and_start_consuming()

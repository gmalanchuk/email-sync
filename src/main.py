import pika

from config import RABBITMQ_USER, RABBITMQ_HOST, RABBITMQ_PASS
from config import logger
from rabbitmq.include_consumers import include_all_consumers


def connection_to_rabbitmq_and_start_consuming():
    credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    logger.info("Rabbitmq connection open")

    include_all_consumers(channel)

    logger.info("Rabbitmq start consuming")
    channel.start_consuming()


if __name__ == '__main__':
    connection_to_rabbitmq_and_start_consuming()

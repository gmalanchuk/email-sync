import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER')
RABBITMQ_PASS = os.environ.get('RABBITMQ_PASS')
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL')

logger.add("email.log", rotation="1 week", format="{level} | {time} | {message}", level=LOGGING_LEVEL)

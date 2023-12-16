import pika

# Подключение к серверу RabbitMQ
credentials = pika.PlainCredentials(username='task', password='task')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='task-rabbitmq', credentials=credentials))
channel = connection.channel()

# Создание очереди (если её нет)
channel.queue_declare(queue='hello')


# Функция, которая будет вызываться при получении сообщения
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


# Указание функции обратного вызова для обработки сообщений
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# Запуск бесконечного цикла ожидания сообщений
channel.start_consuming()

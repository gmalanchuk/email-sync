from rabbitmq.consumers import event_notification


def include_all_consumers_and_queues(channel):
    channel.queue_declare(queue="events", durable=True)
    channel.basic_consume(queue='events', on_message_callback=event_notification, auto_ack=True)

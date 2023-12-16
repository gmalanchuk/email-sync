from rabbitmq.consumers import event_notification


def include_all_consumers(channel):
    channel.basic_consume(queue='events', on_message_callback=event_notification, auto_ack=True)

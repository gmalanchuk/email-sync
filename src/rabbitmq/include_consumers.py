from rabbitmq.consumers import event_notification
from rabbitmq.consumers.calendar import calendar_notification
from rabbitmq.consumers.verification import verification_notification


def include_all_consumers_and_queues(channel):
    channel.queue_declare(queue="events", durable=True)
    channel.basic_consume(queue='events', on_message_callback=event_notification, auto_ack=True)

    channel.queue_declare(queue="calendar", durable=True)
    channel.basic_consume(queue='calendar', on_message_callback=calendar_notification, auto_ack=True)

    channel.queue_declare(queue="verification", durable=True)
    channel.basic_consume(queue='verification', on_message_callback=verification_notification, auto_ack=True)

def event_notification(ch, method, properties, body):
    print(f" [x] Received {body}")

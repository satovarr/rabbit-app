import pika

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()


channel.queue_declare(queue='one_random_queue')

message = "Hello world!"
channel.basic_publish(exchange='', routing_key='one_random_queue', body=message)
print(f"[Producer] Sent: {message}")

def callback(ch, method, properties, body):
    print(f"[Receiver] message received: {body.decode()}")

channel.basic_consume(queue='one_random_queue', on_message_callback=callback, auto_ack=True)

print('[Receiver] Waiting messages...')
channel.start_consuming()

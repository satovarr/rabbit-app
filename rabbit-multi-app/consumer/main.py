from fastapi import FastAPI
import pika
import threading

app = FastAPI()

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='another_random_queue')
    channel.basic_consume(queue='another_random_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

@app.on_event("startup")
def startup_event():
    threading.Thread(target=consume, daemon=True).start()

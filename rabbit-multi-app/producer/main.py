from fastapi import FastAPI, HTTPException
import pika

app = FastAPI()

@app.post("/send/")
def send_message(message: str):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='another_random_queue')
        channel.basic_publish(exchange='', routing_key='another_random_queue', body=message)

        connection.close()
        return {"message": f"Sent '{message}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('prepare_2_rabbitmq'))
channel = connection.channel()

queue = channel.queue_declare('order_notify')
queue_name = queue.method.queue

channel.queue_bind(exchange='order', queue=queue_name, routing_key='order.notify')


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f'Notifying {payload["user_email"]}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue=queue_name)
print('waiting for notify messages')
channel.start_consuming()

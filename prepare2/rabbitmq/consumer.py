import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('prepare_2_rabbitmq'))
channel = connection.channel()

queue = channel.queue_declare('order_report')
queue_name = queue.method.queue
channel.queue_bind(exchange='order', queue=queue_name, routing_key='order.report')


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f'Reporting {payload["user_email"]}')
    print(f'Product: {payload["product"]}')
    print(f'Quantity: {payload["quantity"]}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue=queue_name)
print('waiting for report messages')
channel.start_consuming()

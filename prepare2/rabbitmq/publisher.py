import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('prepare_2_rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='order', exchange_type='direct')

order = {
    'id': str(uuid.uuid4()),
    'user_email': 'john.doe@example.com',
    'product': 'Leather Jacket',
    'quantity': 1,
}

channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'user_email': order['user_email']}),
)
print('sent notify message')

channel.basic_publish(
    exchange='order', routing_key='order.report', body=json.dumps(order)
)
print('sent report message')

connection.close()

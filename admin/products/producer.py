
# amqps://jmbfkave:dI0nCfktSxq7faZbtMEa-s9b3Lm8qvZP@beaver.rmq.cloudamqp.com/jmbfkave

import pika 
params = pika.URLParameters('amqps://jmbfkave:dI0nCfktSxq7faZbtMEa-s9b3Lm8qvZP@beaver.rmq.cloudamqp.com/jmbfkave')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange='', routing_key='main', body='hello')
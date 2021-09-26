# amqps://jmbfkave:dI0nCfktSxq7faZbtMEa-s9b3Lm8qvZP@beaver.rmq.cloudamqp.com/jmbfkave

import pika 
params = pika.URLParameters('amqps://jmbfkave:dI0nCfktSxq7faZbtMEa-s9b3Lm8qvZP@beaver.rmq.cloudamqp.com/jmbfkave')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')



def callback(ch, method, properties, body):
    print('Recevied in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
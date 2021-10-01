# amqps://jmbfkave:dI0nCfktSxq7faZbtMEa-s9b3Lm8qvZP@beaver.rmq.cloudamqp.com/jmbfkave



import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('your cloudamqp url')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')



def callback(ch, method, properties, body):
    print('Recevied in admin')
    print('Recevied in admin',Product.objects.first())
    id = json.loads(body)
    product = Product.objects.get(id=id)
    product.likes =  product.likes + 1
    product.save()
    print('Product likes increased')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
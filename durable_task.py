#-*- encoding=utf8 -*-
import sys
import io
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='durable_queue', durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='durable_queue', body=message, properties=pika.BasicProperties(delivery_mode = 2,))
print " [x] Sent %r" %(message,)
connection.close()

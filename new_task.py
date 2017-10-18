#-*- encoding=utf8 -*-
import sys
import io
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print " [x] Sent %r" %(message,)
connection.close()

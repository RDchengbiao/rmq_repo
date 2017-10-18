#-*- encoding=utf8 -*-
import sys
import io
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='exchange_logs',exchange_type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print " [x] Sent %r:%r" %(severity, message)
connection.close()

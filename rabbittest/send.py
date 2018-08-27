#!/usr/bin/env python
import pika
import sys
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks',durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)

channel.basic_publish(exchange='',
                  routing_key='posts',
                  body=json.dumps(message),
                  properties=pika.BasicProperties(
                     delivery_mode = 2, # make message persistent
                  ))


connection.close()

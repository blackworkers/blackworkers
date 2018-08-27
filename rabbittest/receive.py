#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks',durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(1)
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello')
                      
channel.basic_qos(prefetch_count=1)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

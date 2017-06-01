#_*_coding:utf-8_*_
import pika
import json
import os


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def doing(operation):
    output = subprocess.Popen(operation["command"], shell=True)
    return output

def on_request(ch, method, props, body):
    operation = json.loads(body)

    print(operation["command"])

    response = doing(operation)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=json.dumps(str(response)))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
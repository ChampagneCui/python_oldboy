#_*_coding:utf-8_*_
import pika
import json
import subprocess
import socket
import gevent


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def doing(operation):
    output=subprocess.check_output(operation["command"], shell=True) 
    return output

def on_request(ch, method, props, body):
    operation = json.loads(body)
    if ip in operation["host"]:
        response = doing(operation)
        print(response)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id = \
                                                             props.correlation_id),
                         body=json.dumps(response))
        ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__=='__main__':
    ip=get_ip()
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')
    channel.basic_consume(on_request, queue='rpc_queue')

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

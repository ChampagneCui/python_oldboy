#_*_coding:utf-8_*_
import pika
import json
import subprocess
import socket
import time
import random
import uuid
import socket
import fcntl
import struct

response_dict={}

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def doing(operation):
    try:
        output=subprocess.check_output(operation["command"], shell=True)
    except:
        output="error"
    return output

def on_request(ch, method, props, body):
    operation = json.loads(body)
    if operation.has_key("host") and operation.has_key("command"):
        if ip in operation["host"]:
            new_corr_id = str(random.randint(0,99999))
            #result = ch.queue_declare(exclusive=True)
            #res_queue = result.method.queue
	        ch.queue_declare(new_corr_id)

            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id=props.correlation_id),
                             body=json.dumps(new_corr_id)
                             )

            response = doing(operation)
            response_dict[new_corr_id] = response
            print(response)
            #print(res_queue)
            time.sleep(1)

            ch.basic_publish(exchange='',
                             routing_key=new_corr_id,
                             properties=pika.BasicProperties(correlation_id=new_corr_id,),
                             body=json.dumps(response_dict[new_corr_id])
                             )

            ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    ifname=raw_input('Pls enter the ifname? && eth0 : ')
    ip=get_ip(ifname)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='rpc_ex', type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='rpc_ex',queue=queue_name)
    channel.basic_consume(on_request, queue=queue_name)


    print(" [x] Awaiting RPC requests")
    channel.start_consuming()


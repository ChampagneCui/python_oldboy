#_*_coding:utf-8_*_
import pika
import uuid
import json
import getopt
import sys

operation={}

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)



if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:],"h",["help","host=","command="])
    for op, value in opts:
            if (op == "--host"):
                value=value.split()
                operation["host"]=value
            elif (op == "--command"):
                operation["command"]=value
            else:
                print("run --command='df -h' --hosts=192.168.3.55 10.4.3.4") #help说明
                exit()


    fibonacci_rpc = FibonacciRpcClient()

    print(" [x] Requesting operation")
    response = fibonacci_rpc.call(operation)
    print(" [.] Got %r" % response)
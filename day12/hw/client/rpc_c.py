#_*_coding:utf-8_*_
import pika
import uuid
import getopt
import sys
import json
import time

operation={}
res_dict={}

class RpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='rpc_ex',type='fanout')

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response=json.loads(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='rpc_ex',
                                   routing_key='',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

    def on_res(self, num,ch, method, props, body):
        if num == props.correlation_id:
            self.res_response=json.loads(body)


    def get(self,n):
        self.res_response= None
        self.channel.basic_consume(self.on_res(num=n), queue=self.callback_queue, no_ack=True,)
        while self.res_response is None:
            self.connection.process_data_events()
        return self.res_response

if __name__ == '__main__':
    rpc = RpcClient()
    opts, args = getopt.getopt(sys.argv[1:],"h",["help","host=","command=","check="])
    for op, value in opts:
            if (op == "--host"):
                value=value.split()
                operation["host"]=value
            elif (op == "--command"):
                operation["command"]=value
            elif (op == "--check"):
                a=rpc.get(value)
                print(a)
            else:
                print("run --command='df -h' --hosts=192.168.3.55 10.4.3.4") #help说明
                exit()

    #print(" [x] Requesting operation")
    response = rpc.call(json.dumps(operation))
    print(" [.] task num: %r" % response)


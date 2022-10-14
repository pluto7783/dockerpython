import pika

params = pika.URLParameters('amqps://slwemewz:ve5sumQ4sBZzWc11xdlG7ToH4JJc3paD@dingo.rmq.cloudamqp.com/slwemewz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
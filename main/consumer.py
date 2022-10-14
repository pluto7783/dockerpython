import pika

params = pika.URLParameters('amqps://slwemewz:ve5sumQ4sBZzWc11xdlG7ToH4JJc3paD@dingo.rmq.cloudamqp.com/slwemewz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)
    

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

print('Close')
channel.close()
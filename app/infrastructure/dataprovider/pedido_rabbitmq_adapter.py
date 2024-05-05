# pedido_rabbitmq_adapter.py

import asyncio  # Importe asyncio para operações assíncronas
import pika

class RabbitMQAdapter:
    def __init__(self, amqp_url: str, queue_name: str, durable: bool = True):
        self.amqp_url = amqp_url
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.durable = durable

    def connect(self):
        params = pika.URLParameters(self.amqp_url)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=self.durable)

    async def consume_messages_async(self, callback):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        print('Started consuming messages from RabbitMQ...')
        while True:
            self.connection.process_data_events()  # Processa eventos de dados para evitar bloqueios

    def consume_messages(self, callback):
        asyncio.create_task(self.consume_messages_async(callback))  # Inicia o consumo em um processo assíncrono

    def close_connection(self):
        if self.connection:
            self.connection.close()

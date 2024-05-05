import pika
import threading
from sqlalchemy.orm import Session
from core.ports.pedido_repository import PedidoRepository
from core.model.pedido import Pedido as PedidoModel


class PedidoServiceImpl:
    def __init__(self, pedido_repository: PedidoRepository):
        self.pedido_repository = pedido_repository
        self.db = Session

        amqp_url = "amqp://guest:guest@172.20.0.3:5672/"
        #print('Started Consuming')
        params = pika.URLParameters(amqp_url)
        params.socket_timeout = 5
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='createOrder')
        self.channel.basic_consume(queue='createOrder', on_message_callback=self.callback, auto_ack=True)
        print('Started Consuming')

        threading.Thread(target=self.start_consuming_in_thread).start()

        #self.channel.close()
    def start_consuming_in_thread(self):
        self.channel.start_consuming()
        #self.channel.close()

    def callback(self, ch, method, properties, body):
        pedido_id = int(body)
        #database = Session
        #print(self)
        db = Session()
        print(" ---- ")
        #print(database)
        self.pedido_repository.atualizar_status_para_preparacao(db, pedido_id)

    def create_pedido(self, db: Session, pedido: PedidoModel):
        return self.pedido_repository.create_pedido(db, pedido)

    def get_pedidos(self, db: Session, skip: int = 0, limit: int = 100):
        return self.pedido_repository.get_pedidos(db, skip, limit)

    def get_pedidos_by_status(
        self, db: Session, status: int, skip: int = 0, limit: int = 100
    ):
        return self.pedido_repository.get_pedidos_by_status(db, status, skip, limit)

    def atualizar_status_para_preparacao(self, db: Session, pedido_id: int):
        return self.pedido_repository.atualizar_status_para_preparacao(db, pedido_id)

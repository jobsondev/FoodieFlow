from sqlalchemy.orm import Session
from core.ports.pedido_repository import PedidoRepository
from core.model.pedido import Pedido as PedidoModel
from infrastructure.dataprovider.pedido_rabbitmq_adapter import RabbitMQAdapter

class PedidoUseCase:
    def __init__(self, pedido_repository: PedidoRepository, rabbitmq_adapter: RabbitMQAdapter):
        self.pedido_repository = pedido_repository
        self.rabbitmq_adapter = rabbitmq_adapter

    def callback_rabbitmq(self, ch, method, properties, body):
        pedido_id = int(body)
        print(f"Received message with self: {self}")
        print(f"Converted pedido_id: {pedido_id}")
        print(f"Pedido {pedido_id} atualizado para status 2")
        
        try:
            #with Session() as db:
                db = Session()
                print(f"db {db}")
                self.pedido_repository.atualizar_status_para_preparacao(1, 1)
                print(f"Pedido {pedido_id} atualizado com sucesso.")
        except Exception as e:
            print(f"Error updating pedido {pedido_id}: {e}")

    def iniciar_consumidor_rabbitmq(self):
        print("Starting RabbitMQ consumer...")
        self.rabbitmq_adapter.consume_messages(self.callback_rabbitmq)

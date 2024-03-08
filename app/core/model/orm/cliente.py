from infrastructure.database import Base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    cpf = Column(VARCHAR(11), unique=True, index=True, nullable=False)
    nome = Column(VARCHAR(255))
    email = Column(VARCHAR(255))

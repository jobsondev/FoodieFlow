from sqlalchemy import Column, ForeignKey, Integer, String, Table

from infrastructure.database import Base

# Tabela associativa para o relacionamento entre Produto e Ingrediente
produto_ingrediente = Table(
    "produto_ingrediente",
    Base.metadata,
    Column("id_produto", Integer, ForeignKey("produto.id")),
    Column("id_ingrediente", Integer, ForeignKey("ingrediente.id")),
)


class Ingrediente(Base):
    __tablename__ = "ingrediente"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

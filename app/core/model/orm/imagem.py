from sqlalchemy import Column, ForeignKey, Integer, String

from infrastructure.database import Base


class Imagem(Base):
    __tablename__ = "imagem"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caminho = Column(String, nullable=False)
    id_produto = Column(Integer, ForeignKey("produto.id"), nullable=False)

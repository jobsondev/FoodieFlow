from typing import List, Optional

from core.model.imagem import Imagem
from core.model.ingrediente import Ingrediente
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    imagens: List[str] = []
    ingredientes: List[int] = []
    preco: float
    id_categoria: int


class Produto(ProdutoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class ProdutoCompleto(Produto):
    imagens: List[Imagem]
    ingredientes: List[Ingrediente]

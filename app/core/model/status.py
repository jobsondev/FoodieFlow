from typing import Optional
from pydantic import BaseModel


class Status(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None

    class Config:
        from_attributes = True

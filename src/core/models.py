from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False
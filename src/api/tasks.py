from fastapi import APIRouter
from src.core.models import Tarefa

router = APIRouter()  # <--- Esta linha é a que está a faltar! 🚀

@router.post("/tarefas")
def criar_tarefa(nova_tarefa: Tarefa):
    return {"mensagem": "Tarefa criada!", "dados": nova_tarefa}
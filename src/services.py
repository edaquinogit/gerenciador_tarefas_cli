from src.models import Tarefa
from src.storage import carregar_tarefas, salvar_tarefas

def adicionar(descricao: str) -> None:
    tarefas = carregar_tarefas()
    nova = Tarefa(descricao=descricao)
    tarefas.append(nova)
    salvar_tarefas(tarefas)

def listar() -> list[Tarefa]:
    return carregar_tarefas()

def remover(indice: int) -> None:
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)

def concluir(indice: int) -> None:
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
      tarefas[indice].status = 'Concluida'
      salvar_tarefas(tarefas)

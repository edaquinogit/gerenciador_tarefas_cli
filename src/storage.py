import json
from pathlib import Path
from typing import List
from src.models import Tarefa

ARQUIVO_TAREFAS = Path('tarefas.json')

def carregar_tarefas() -> List[Tarefa]:
    if not ARQUIVO_TAREFAS.exists():
        return []
    try: 
        if ARQUIVO_TAREFAS.stat().st_size == 0:
            return[]
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return[]
        
        return [Tarefa.from_dict(item) for item in data]
    except (json.JSONDecodeError, OSError):

       return[]

    
def salvar_tarefas(tarefas: List[Tarefa]) -> None:
    with open(ARQUIVO_TAREFAS, 'w',  encoding='utf-8') as f:
        json.dump([t.to_dict() for t in tarefas], f, ensure_ascii=False, ident=2)

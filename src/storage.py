import json
import os
from src.models import Tarefa

CAMINHO_ARQUIVO = os.path.join("data", "tarefas.json")


def salvar_tarefas(tarefas):
    os.makedirs("data", exist_ok=True)
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(
            [t.to_dict() for t in tarefas],
            f,
            ensure_ascii=False,
            indent=2
        )


def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return [Tarefa.from_dict(d) for d in dados]
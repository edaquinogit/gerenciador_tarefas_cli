import json
import os

ARQUIVO_TAREFAS = "tasks.json"

def carregar_tarefas():
    """Carrega a lista de tarefas do arquivo JSON"""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON"""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def add_tasks(*novas_tarefas):
    """Adiciona uma ou mais tarefas, evitando duplicatas"""
    tarefas = carregar_tarefas()
    for tarefa in novas_tarefas:
        if tarefa not in tarefas:
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada!")
        else:
            print(f"Tarefa '{tarefa}' já existe.")
    salvar_tarefas(tarefas)

def remove_tasks(*tarefas_remover):
    """Remove uma ou mais tarefas"""
    tarefas = carregar_tarefas()
    for tarefa in tarefas_remover:
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa}' removida!")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")
    salvar_tarefas(tarefas)

def list_tasks():
    """Retorna a lista atual de tarefas"""
    return carregar_tarefas()

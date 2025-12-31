# src/tasks.py

tasks = []

def add_task(title):
    tasks.append(title)
    return f"Tarefa '{title}' adicionada!"

def list_tasks():
    return tasks

def remove_task(index):
    try:
        removed = tasks.pop(index)
        return f"Tarefa '{removed}' removida!"
    except IndexError:
        return "Índice inválido."
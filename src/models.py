# src/models.py
class Tarefa:
    def __init__(self, titulo, status="pendente"):
        self.titulo = titulo
        self.status = status

    def __repr__(self):
        return f"<Tarefa titulo={self.titulo} status={self.status}>"
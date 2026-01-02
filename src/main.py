from fastapi import FastAPI
from src.api.tasks import router as tasks_router

app = FastAPI()

# Inclui as rotas do ficheiro tasks.py
app.include_router(tasks_router)

@app.get("/")
def raiz():
    return {"mensagem": "API de Tarefas Online!"}
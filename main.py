import json
import os

# Nome do arquivo onde as tarefas serão salvas
ARQUIVO_DADOS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(tarefas, f, indent=4)

def menu():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n--- GERENCIADOR DE TAREFAS (CLI) ---")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nSua Lista de Tarefas:")
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t['titulo']} - {t['status']}")
        
        elif opcao == "2":
            titulo = input("Título da tarefa: ")
            tarefas.append({"titulo": titulo, "status": "pendente"})
            salvar_tarefas(tarefas)
            print("Tarefa adicionada com sucesso!")
            
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
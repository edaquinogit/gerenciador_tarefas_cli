from src.tasks import add_tasks, list_tasks, remove_tasks

def mostrar_tarefas():
    tarefas = list_tasks()
    if tarefas:
        print("\nTarefas atuais:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("\nNenhuma tarefa cadastrada.")

def main():
    while True:
        print("\n=== GERENCIADOR DE TAREFAS CLI ===")
        mostrar_tarefas()
        print("\n1 - Adicionar tarefas")
        print("2 - Remover tarefas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tarefas_input = input("Digite as tarefas separadas por vírgula: ")
            tarefas = [t.strip() for t in tarefas_input.split(",")]
            add_tasks(*tarefas)

        elif opcao == "2":
            tarefas_input = input("Digite as tarefas para remover, separadas por vírgula: ")
            tarefas = [t.strip() for t in tarefas_input.split(",")]
            remove_tasks(*tarefas)

        elif opcao == "3":
            print("Saindo do gerenciador...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


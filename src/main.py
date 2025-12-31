from src.tasks import add_tasks, list_tasks, remove_tasks
from colorama import init, Fore, Style

init(autoreset=True)

def mostrar_tarefas():
    tarefas = list_tasks()
    if tarefas:
        print(Fore.CYAN + "\nTarefas atuais:")
        for i, tarefa in enumerate(tarefas, 1):
            print(Fore.YELLOW + f"{i}. {tarefa}")
    else:
        print(Fore.CYAN + "\nNenhuma tarefa cadastrada.")

def main():
    while True:
        print(Fore.GREEN + "\n=== GERENCIADOR DE TAREFAS CLI ===")
        mostrar_tarefas()
        print("\n1 - Adicionar tarefas")
        print("2 - Remover tarefas")
        print("3 - Sair")

        opcao = input(Fore.WHITE + "Escolha uma opção: ").strip()

        if opcao == "1":
            tarefas_input = input(Fore.WHITE + "Digite as tarefas separadas por vírgula: ")
            tarefas = [t.strip() for t in tarefas_input.split(",")if t.strip()]

            if tarefas:
                add_tasks(*tarefas)
            else:
                print(Fore.RED + "Nenhuma tarefa válida foi digitada!")

        elif opcao == "2":
            tarefas = list_tasks()
            if not tarefas:
                print(Fore.RED + "Nenhuma tarefa para remover.")
                continue

            mostrar_tarefas()
            indices_input = input(Fore.WHITE + "Digite os números das tarefas para remover, separados por vírgula: ")

            try:
                indices = [int(i.strip()) - 1 for i in indices_input.split(",")]
                tarefas_para_remover = []
                for i in indices:
                    if 0 <= i < len(tarefas):
                        tarefas_para_remover.append(tarefas[i])
                    else:
                        print(Fore.RED + f"Número {i+1} inválido, ignorando.")
                remove_tasks(*tarefas_para_remover)
            except ValueError:
                print(Fore.RED + "Entrada inválida! Digite apenas números separados por vírgula.")

        elif opcao == "3":
            print(Fore.GREEN + "Saindo do gerenciador...")
            break

        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

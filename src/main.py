from src.models import Tarefa
from src.storage import salvar_tarefas, carregar_tarefas
from src.tasks import add_task, list_tasks, remove_task


def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa(s)")
    print("5 - Sair")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa.status == "Concluida" else "Pendente"
        print(f"{i}. [{status}] {tarefa.descricao}")


def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()
    if descricao:
        tarefas.append(Tarefa(descricao))
        print("Tarefa adicionada com sucesso.")
    else:
        print("Descrição inválida.")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa para concluir: "))
        tarefas[indice - 1].concluir()
        print("Tarefa concluída.")
    except (ValueError, IndexError):
        print("Número inválido.")


def excluir_tarefas(tarefas):
    listar_tarefas(tarefas)

    entrada = input(
        "Digite os números das tarefas para excluir (ex: 1,3,5): "
    )

    try:
        indices = sorted(
            {int(i.strip()) - 1 for i in entrada.split(",")},
            reverse=True
        )

        for i in indices:
            if 0 <= i < len(tarefas):
                tarefas.pop(i)

        print("Tarefa(s) excluída(s) com sucesso.")
    except ValueError:
        print("Entrada inválida.")


def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)

        elif opcao == "4":
            excluir_tarefas(tarefas)
            salvar_tarefas(tarefas)

        elif opcao == "5":
            print("Saindo... até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


def print_help():
    print("Uso:")
    print("python src/main.py add \"Título da tarefa\"")
    print("python src/main.py list'")
    print("python src/main.py remove <indice>")

if __name__ == "__main__":
    print(add_task("Estudar Python"))
    print(list_tasks())
    print(remove_task(0))
from src.services import adicionar, listar, remover, concluir

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Concluir tarefa")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            descricao = input("Descricao: ")
            adicionar(descricao)
        elif opcao == "2":
            for i, tarefa in enumerate(listar()):
                print(f"{i}. {tarefa.descricao} - {tarefa.status}")
        elif opcao == "3":
            indice = int(input("Indice da tarefa: "))
            remover(indice)
        elif opcao == "4":
            indice = int(input("Indice da tarefa: "))
            concluir(indice)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
# main.py

def exibir_menu():
    print('\n=== GERENCIADOR DE TAREFAS ===')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Sair')


def main():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção:')

        if opcao == '1':
            print('Funcionalidade de adicionar tarefa em desenvolvimento.')
        elif opcao == '2':
            print('Funcionalidade de adicionar tarefas em desenvolvimento.')
        elif opcao == '3':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')
    

 
if __name__ == '__main__':
    main()

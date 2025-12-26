tarefas = []

def exibir_menu():
    '''
    Exibe o menu principal do gerenciador de tarefas.
    '''
    print('\n--- GERENCIADOR DE TAREFAS ---')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Sair')


def adicionar_tarefa():
    '''
   Adiciona uma nova tarefa à lista.
   '''
    descricao = input('Digite a descrição da tarefa:')
    if descricao.strip() == '':
        print('A tarefa não pode ser vazia.')
    else:
        tarefas.append(descricao)
        print('Tarefa adicionada com sucesso!')

    
def listar_tarefas():
    '''
    Lista todas as tarefas cadastradas.
    '''
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('\n--- TAREFAS ---')
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f'{indice}. {tarefa}')

def main():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção:')

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            print('Saindo do programa. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()

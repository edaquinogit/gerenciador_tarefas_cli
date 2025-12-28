import json
import os

ARQUIVO_TAREFAS = 'tarefas.json'

def exibir_menu():
    '''
    Exibe o menu principal do gerenciador de tarefas.
    '''
    print('\n--- GERENCIADOR DE TAREFAS ---')
    print('\n1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')


def adicionar_tarefa():
    ...
    '''
   Adiciona uma nova tarefa à lista.
   '''
    descricao = input('Digite a descrição da tarefa:')
    if descricao.strip() == '':
        print('A tarefa não pode ser vazia')
        return
    
    tarefas.append(descricao)
    salvar_tarefas(tarefas)
    print('Tarefa adicionada com sucesso!')
    

    
def listar_tarefas():
    ...
    '''
    Lista todas as tarefas cadastradas.
    '''
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('\n--- TAREFAS ---')
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f'{indice}. {tarefa}')


def remover_tarefa():
    ...
    '''
    Remove uma tarefa da lista.
    '''
    if len(tarefas) == 0:
        print('nenhuma tarefa cadrastrada para remover.')
        return

    listar_tarefas()

    try:
        indice = int(input('Digite o numero da tarefa que deseja remover:'))
        tarefa_removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f'Tarefa removida: {tarefa_removida}')
    except (ValueError, IndexError):
        print('Opção inválida. tente novamente.')


def carregar_tarefas():
    ...
    '''
    Carrega as tarefas do arquivo JSON.
    '''
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, 'r', encoding= 'utf-8') as arquivo:
        return json.load(arquivo)
    
def salvar_tarefas(tarefas):
    ...
    '''
    Salva as tarefas no arquivo JSON.
    '''
    with open(ARQUIVO_TAREFAS, 'w', encoding= 'utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

def main():
    ...
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção:')

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '4':
            print('Saindo do programa. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    tarefas = carregar_tarefas()
    main()

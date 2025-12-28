import json
import os

ARQUIVO_TAREFAS = 'tarefas.json'

#------------------------
# Persistencia de dados
# -----------------------

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    
    with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

# -----------------------
# Funcionalidades
# -----------------------
def adicionar_tarefa(tarefas):
    descricao = input('Digite a descrição da Tarefa:').strip()

    if not descricao:
        print('A tarefa não pode ser vazia!')
        return tarefas
    
    nova_tarefa = {'descricao': descricao, 'status': 'pendente'}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    print('Tarefa adicionada com sucesso')
    return tarefas

def listar_tarefas(tarefas):
    print('\n--- TAREFAS ---')

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa['descricao']} - {tarefa['status']}')
            

            input('\nPressione ENTER para voltar ao menu...')
        

def remover_tarefa(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para remover.')
        input('Pressione ENTER para voltar ao menu...')
        return tarefas
    
    listar_tarefas(tarefas)

    try:
        indice = int(input('Digite o número da tarefa:'))
        tarefa_removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f'Tarefa removida: {tarefa_removida}')
    except (ValueError, IndexError):
        print('Número invalido.')

        input('Pressione ENTER para voltar ao menu')
        return tarefas
    

# -----------------------
# Interface do úsuario
# -----------------------
def exibir_menu():
    print('\n--- GERENCIADOR DE TAREFAS ---')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Remover tarefa')
    print('0. Sair')


def main():
    tarefas = carregar_tarefas()

    while True:
        print('\n1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Remover tarefa')
        print('0. Sair')


        opcao = input('Escolha uma opção:')

        if opcao == '1':
            tarefas = adicionar_tarefa(tarefas)

        elif opcao == '2':
            listar_tarefas(tarefas)

        elif opcao == '3':
            tarefas = remover_tarefa(tarefas)

        elif opcao == '0':
            print('Saindo do programa. Até logo!')
            break

        else:
            print('Opção invalida')


# -----------------------
# Execução
# -----------------------
if __name__ == '__main__':
    main()
import os
def criar_arquivo():
    '''Cria um arquivo txt com um cabeçalho específico '''
    with open('TAREFAS.txt','w',encoding='utf-8') as arquivo:
        arquivo.write('LISTA DE TAREFAS\n')

if __name__=='__main__':
    criar_arquivo()


def obter_contador():
    """Retorna o próximo número disponível para uma tarefa."""

    try:
        with open('TAREFAS.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        return len(linhas)

    except FileNotFoundError:
        return 1

def adiciona_tarefa(cont):
    ''' Adiciona nova tarefa na lista'''
    tarefa=input('Informe a tarefa:')
    tarefa=tarefa.upper()
    try:
        with open('TAREFAS.txt','a') as arquivo:
            arquivo.write(f'{cont}--{tarefa}\n')
    except:
        print('Erro')

    pass
def lista_tarefa():
    '''Lista as tarefas da lista'''
    with open('TAREFAS.txt','r') as arquivo:
        conteudo=arquivo.readlines()

    for linha in conteudo:
        print(linha.strip())


def remove_tarefa():
    ''' Remove tarefas da lista'''
    '''*ler todas as tarefas em forma de lista e depois retirar elas '''
    lista_tarefa()
    with open('TAREFAS.txt','r') as arquivo:
        linhas=arquivo.readlines()
    
    item_remover=int(input('\nInforme o item que gostaria de remover:'))
    del linhas[item_remover-1]

    with open('TAREFAS.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
       
    pass
def limpa_tarefa():
    '''limpa tarefas da lista'''
    with open('TAREFAS.txt','w',encoding='utf-8') as arquivo:
        arquivo.write('LISTA DE TAREFAS\n')

def menu():
    """Menu de interação."""

    tarefa = -1
    cont = obter_contador()

    try:
        while tarefa != 0:

            print('''
            ===== LISTA DE TAREFAS =====

                1 - Adicionar tarefa
                2 - Listar tarefas
                3 - Remover tarefa
                4 - Limpar tarefas
                0 - Sair
            ''')

            tarefa = int(input('Informe a opção: '))

            if tarefa == 1:
                adiciona_tarefa(cont)
                cont += 1

            elif tarefa == 2:
                lista_tarefa()

            elif tarefa == 3:
                pass

            elif tarefa == 4:
                limpa_tarefa()

    except ValueError:
        print('Digite apenas números.')


if __name__=='__main__':
    menu()

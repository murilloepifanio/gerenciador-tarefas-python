# Lista de Tarefas em Python

Projeto desenvolvido em **Python** para praticar manipulação de arquivos e conceitos fundamentais da linguagem através de um sistema de gerenciamento de tarefas executado pelo terminal.

O programa permite adicionar, visualizar, remover e limpar tarefas, mantendo os dados armazenados em um arquivo `.txt`.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

* Criar automaticamente um arquivo para armazenar as tarefas
* Adicionar novas tarefas
* Listar as tarefas cadastradas
* Remover uma tarefa específica
* Limpar todas as tarefas
* Numerar as tarefas cadastradas
* Armazenar as informações em arquivo `.txt`
* Menu interativo no terminal

## Menu do sistema

Ao executar o programa, o seguinte menu é apresentado:

```text
===== LISTA DE TAREFAS =====

1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Limpar tarefas
0 - Sair
```

## Armazenamento dos dados

Diferentemente de um programa que mantém os dados apenas em listas durante sua execução, este projeto utiliza um arquivo chamado:

```text
TAREFAS.txt
```

As tarefas são armazenadas no arquivo para que possam ser acessadas posteriormente.

Exemplo:

```text
LISTA DE TAREFAS
1--ESTUDAR PYTHON
2--FAZER EXERCÍCIOS
3--ATUALIZAR GITHUB
```

## Conceitos de Python utilizados

Durante o desenvolvimento deste projeto foram utilizados:

* Funções
* Manipulação de arquivos
* `open()`
* `with`
* Modos de abertura `r`, `w` e `a`
* `readlines()`
* `writelines()`
* `write()`
* Listas
* `del`
* Laço `while`
* Laço `for`
* Estruturas condicionais
* `try` e `except`
* `FileNotFoundError`
* `ValueError`
* Contadores
* Conversão com `int()`
* Método `.upper()`
* Método `.strip()`
* Encoding UTF-8
* `if __name__ == "__main__"`

## Organização do programa

O projeto foi dividido em funções com responsabilidades específicas:

```text
criar_arquivo()
    ↓
Cria o arquivo TAREFAS.txt

obter_contador()
    ↓
Determina a numeração da próxima tarefa

adiciona_tarefa()
    ↓
Adiciona uma nova tarefa ao arquivo

lista_tarefa()
    ↓
Exibe as tarefas armazenadas

remove_tarefa()
    ↓
Remove uma tarefa selecionada

limpa_tarefa()
    ↓
Remove todas as tarefas e recria o cabeçalho

menu()
    ↓
Controla a interação com o usuário
```

## Modos de abertura de arquivos utilizados

Neste projeto foram utilizados diferentes modos de manipulação de arquivos.

### Leitura — `r`

Utilizado para consultar o conteúdo existente:

```python
with open('TAREFAS.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
```

### Escrita — `w`

Utilizado quando é necessário sobrescrever o conteúdo:

```python
with open('TAREFAS.txt', 'w') as arquivo:
    arquivo.writelines(linhas)
```

### Adição — `a`

Utilizado para adicionar novas tarefas sem apagar as existentes:

```python
with open('TAREFAS.txt', 'a') as arquivo:
    arquivo.write(f'{cont}--{tarefa}\n')
```

## Tratamento de erros

O programa utiliza tratamento de exceções para lidar com algumas situações inesperadas.

Por exemplo, caso o arquivo ainda não exista:

```python
except FileNotFoundError:
    return 1
```

Também existe tratamento para entradas inválidas no menu:

```python
except ValueError:
    print('Digite apenas números.')
```

## Como executar

Tenha o Python instalado no computador.

Clone o repositório:

```bash
git clone https://github.com/murilloepifanio/gerenciador-tarefas-python.git
```

Entre na pasta:

```bash
cd gerenciador-tarefas-python
```

Execute:

```bash
python main.py
```

## Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos de **Python**, principalmente para colocar em prática conceitos relacionados à manipulação e persistência de dados utilizando arquivos.

O projeto representa uma evolução dos exercícios que armazenavam informações apenas em variáveis, listas e dicionários durante a execução do programa.

## Próximas melhorias

Algumas melhorias planejadas para o projeto:

* Melhorar a validação das opções do menu
* Impedir a remoção de posições inexistentes
* Renumerar automaticamente as tarefas após uma exclusão
* Verificar automaticamente se o arquivo já existe
* Melhorar o tratamento de exceções
* Separar responsabilidades em diferentes módulos
* Migrar o armazenamento de `.txt` para JSON
* Criar uma versão utilizando SQLite
* Implementar orientação a objetos
* Criar testes automatizados

## Autor

**Murillo Epifânio de Almeida**

Projeto desenvolvido para fins de estudo e prática de programação em Python.

# DESAFIO 115
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade 
# em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa 
# e listar todas as pessoas cadastradas.

from ex115_md import *
from time import sleep

arq = 'cev.txt'
if not arqex(arq):
    criarq(arq)

while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if r == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarq(arq)
        sleep(2)
    elif r == 2:
        # Opção de cadastrar uma nova pessoa
        tit('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadast(arq, nome, idade)
    elif r == 3:
        tit('Saindo do sistema... Até logo!')
        break
    else:
        print(vermelho + 'ERRO! Digite uma opção válida.' + rc)
        sleep(2)
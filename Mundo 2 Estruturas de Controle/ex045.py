# DESAFIO 045
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print('Olá, vamos jogar Jokenpô!')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
jog = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'Computador jogou: {comp}')
print(f'Jogador jogou: {lista[jog]}')
print('-=' * 12)
if comp == lista[0]:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCE')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if comp == lista[1]:
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if comp == lista[2]:
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

# DESAFIO 028
# Escreva um programa que faça o computador escolher um número entre 0 e 5 e peça para o usuário tentar
# adivinhar o número escolhido. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num = randint(0, 5)
esc = int(input('Tente adivinhar um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
print(f'O número escolhido pelo computador foi {num}')
if esc == num:
    print('PARABÉNS!! Você acertou!')
else:
    print('Que pena! Você perdeu!')

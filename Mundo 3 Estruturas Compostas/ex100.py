# DESAFIO 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e coloca-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia():
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    for v in numeros:
        print(f'{v} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    s = 0
    for v in numeros:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {numeros}, temos: {s}')


numeros = []
sorteia()
somapar()

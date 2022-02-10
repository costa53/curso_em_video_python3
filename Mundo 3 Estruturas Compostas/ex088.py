# DESAFIO 088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
# em uma lista composta.

from random import randint
from time import sleep

sorteados = []
jogos = []
print('–' * 30)
print(f'{"MEGA SENA":^30}')
print('–' * 30)
n = int(input('Quantos jogos você quer gerar? '))
print()
print('–=' * 3, f'SORTEANDO {n} JOGOS', '–=' * 3)
for v in range(0, n):
    for i in range(0, 6):
        num = randint(1, 60)
        while num in jogos:
            num = randint(1, 60)
        jogos.append(num)
        jogos.sort()
    sorteados.append(jogos[:])
    jogos.clear()
    print(f'Jogo {v+1}: {sorteados[v]}')
    sleep(0.5)
print('–=' * 4, 'BOA SORTE!!!', '–=' * 4)

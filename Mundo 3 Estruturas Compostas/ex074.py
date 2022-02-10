# DESAFIO 074
# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre
# a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteados = ()
for s in range(0, 5):
    num = randint(1, 10)
    while num in sorteados:
        num = randint(1, 10)
    sorteados += num,
print(f'Os valores sorteados foram: {sorteados}')
print(f'O maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')

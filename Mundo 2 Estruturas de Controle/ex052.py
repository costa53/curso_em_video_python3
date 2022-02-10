# DESAFIO 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(c, end=' ')
        total += 1
if total == 2:
    print(f'\nO número {num} é um NÚMERO PRIMO')
else:
    print(f'\nO número {num} NÃO é um NÚMERO PRIMO')

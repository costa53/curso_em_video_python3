# DESAFIO 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre:
# qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.

valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {i}: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor {max(valores)} foi digitado na posição ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}...', end='')
print(f'\nO valor {min(valores)} foi digitado na posição ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}...', end='')

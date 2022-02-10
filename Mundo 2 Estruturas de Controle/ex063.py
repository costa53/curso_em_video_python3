# DESAFIO 063
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma Sequência de Fibonacci. Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8.

print('-=' * 20)
print(f'{"Sequência de Fibonacci":^40}')
print('-=' * 20)
num = int(input('Quantos termos você quer mostrar? '))
print('~~' * 20)
t1 = 0
t2 = 1
cont = 3
print(f'{t1} ➝ {t2}', end='')
while cont <= num:
    t3 = t1 + t2
    print(f' ➝ {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➝ FIM')
print('~~' * 20)

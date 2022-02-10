# DESAFIO 060
# Faça um programa que leia um número qualquer e mostre seu fatorial. Ex: 5!=5x4x3x2x1=120

n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')

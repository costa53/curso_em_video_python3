# DESAFIO 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} vale {d}. \nO triplo de {n} vale {t}.')
print(f'A raiz quadrada de {n} é igual a {r:.2f}')

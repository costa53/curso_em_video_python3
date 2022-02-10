# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente.

from math import radians, cos, sin, tan

a = float(input('Digite um ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O ângulo de {a} tem o SENO de {s:.2f}')
print(f'O ângulo de {a} tem o COSSENO de {c:.2f}')
print(f'O ângulo de {a} tem a TANGENTE de {t:.2f}')

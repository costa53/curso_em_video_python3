# DESAFIO 096
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    x = l * c
    print(f'A área de um terreno {l}x{c} é de {x:.1f}m²')


area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

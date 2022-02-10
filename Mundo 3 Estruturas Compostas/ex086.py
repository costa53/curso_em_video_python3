# DESAFIO 086
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

valores = [[], [], []]
for c in range(0, 3):
    for v in range(0, 3):
        valores[c].append(int(input(f'Digite um valor para [{c}, {v}]: ')))
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{valores[c][v]:^3}]', end='')
    print()

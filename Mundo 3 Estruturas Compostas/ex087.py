# DESAFIO 087
# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

valores = [[], [], []]
soma = pares = maior = 0
for c in range(0, 3):
    for v in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {v}]: '))
        valores[c].append(num)
        if num % 2 == 0:
            pares += num
        if v == 2:
            soma += num
        if c == 1 and num > maior:
            maior = num
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{valores[c][v]:^3}]', end='')
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(valores[1])} e {maior}')

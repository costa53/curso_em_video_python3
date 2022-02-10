# DESAFIO 082
# Crie um programa que leia vários números e coloque-os em uma lista. Depois disso, crie 2 listas extras
# que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das 3 listas geradas.

valores = []
vpares = []
vimpares = []
while True:
    valores.append(int(input('Digite um número: ')))
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
for v in valores:
    if v % 2 == 0:
        vpares.append(v)
    elif v % 2 == 1:
        vimpares.append(v)
print('=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {vpares}')
print(f'A lista de ímpares é {vimpares}')

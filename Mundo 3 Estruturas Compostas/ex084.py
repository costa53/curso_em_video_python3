# DESAFIO 084
# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) uma listagem
# com as pessoas mais leves.

info = []
coleta = []
peso = []
nome = []
while True:
    coleta.append(str(input('Nome: ')))
    coleta.append(float(input('Peso: ')))
    info.append(coleta[:])
    peso.append(coleta[:][1])
    nome.append(coleta[:][0])
    coleta.clear()
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
print(f'Ao todo, você cadastrou {len(info)} pessoas.')
print(f'O maior peso de {max(peso)}Kg foi de ', end='')
for v, i in enumerate(peso):
    if i == max(peso):
        print(f'[{nome[v]}] ', end='')
print(f'\nO menor peso de {min(peso)}Kg foi de ', end='')
for v, i in enumerate(peso):
    if i == min(peso):
        print(f'[{nome[v]}] ', end='')

# DESAFIO 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam
# mais de R$ 1000. C) Qual é o nome do produto mais barato.

totmil = cont = total = menor = 0
barato = ''
print('–' * 30)
print(f'{"MERCADO BIG":^30}')
print('–' * 30)
while True:
    nome = str(input('Nome do produto: '))
    pr = float(input('Preço: R$'))
    cont += 1
    total += pr
    if pr > 1000:
        totmil += 1
    if cont == 1 or pr < menor:
        menor = pr
        barato = nome
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
print(f'{" FIM DO PROGRAMA ":=^29}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

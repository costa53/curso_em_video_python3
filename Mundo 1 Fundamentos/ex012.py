# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pr = float(input('Qual é o preço do produto? R$'))
desc = 5
pf = pr - (pr * desc / 100)
print(f'O produto que custava R${pr:.2f}, na promoção com desconto de {desc}% vai custar R${pf:.2f}')

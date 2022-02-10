# DESAFIO 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
ano = float(input('Em quantos anos de financiamento? '))
pres = valor / (ano * 12)
if pres <= (sal * 30) / 100:
    print(f'O empréstimo foi APROVADO! \nA prestação mensal será de R${pres:.2f}')
else:
    print('O empréstimo foi NEGADO!')

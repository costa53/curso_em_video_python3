# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual é o salário do funcionário? R$'))
aum = 15
novo = sal + (sal * aum / 100)
print(f'Um funcionário que ganhava R${sal:.2f}, com {aum}% de aumento, passa a receber R${novo:.2f}')

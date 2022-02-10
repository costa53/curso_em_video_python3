# DESAFIO 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

dis = float(input('Qual a distância da viagem em Km? '))
if dis <= 200:
    pr = dis * 0.50
else:
    pr = dis * 0.45
print(f'O preço da passagem é R${pr:.2f}')

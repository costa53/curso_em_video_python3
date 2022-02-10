# DESAFIO 071
# Crie um programa que simule o financiamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues. OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
for ced in [50, 20, 10, 1]:
    totced = valor // ced
    valor = valor % ced
    if totced > 0:
        print(f'Total de {totced} cédulas de R${ced}')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

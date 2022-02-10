# DESAFIO 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratação'] - nasc + 35
for k, v in dados.items():
    print(f'— {k:<10} tem o valor {v}')

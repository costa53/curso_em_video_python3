# DESAFIO 041
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM, até 14 anos: INFANTIL,
# até 19 anos: JÚNIOR, até 25 anos: SÊNIOR e acima: MASTER.

from datetime import date

ano = date.today().year
nasc = int(input('Qual o ano de nascimento do atleta? '))
idade = ano - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

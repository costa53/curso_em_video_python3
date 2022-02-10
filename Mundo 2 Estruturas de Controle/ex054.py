# DESAFIO 054
# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores (21 anos).

from datetime import date
ano = date.today().year
cont = 0
contm = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if nasc <= ano - 21:
        cont += 1
    else:
        contm += 1
print(f'Ao todo tivemos {cont} pessoas maiores de idade')
print(f'E também tivemos {contm} pessoas menores de idade')

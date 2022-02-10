# DESAFIO 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar e
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou o que passou do prazo.

from datetime import date

ano = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc
if idade < 17:
    tempo = 18 - idade
    print(f'Falta {tempo} anos para você se alistar ao serviço militar.')
elif idade == 17:
    print('Falta 1 ano para você se alistar ao serviço militar.')
elif idade == 18:
    print('Está na hora de você se alistar ao serviço militar!')
elif idade == 19:
    print('Passou 1 ano do prazo para você se alistar.')
else:
    tempo = idade - 18
    print(f'Passou {tempo} anos do prazo para você se alistar.')

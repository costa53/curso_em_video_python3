# DESAFIO 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
# número no dado.

from random import randint
from time import sleep

dados = dict()
for c in range(0, 4):
    dados[f'jogador{c+1}'] = randint(1, 6)
print('Valores Sorteados:')
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
for k, v in enumerate(sorted(dados.items(), key=lambda x: x[1], reverse=True)):
    print(f'{k+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)

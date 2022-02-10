# DESAFIO 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jog = dict()
gol = list()
jog['nome'] = str(input('Nome do Jogador: ')).title()
n = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
for c in range(1, n+1):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
jog['gols'] = gol[:]
jog['total'] = sum(gol)
print('–=' * 30)
print(jog)
print('–=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}.')
print('–=' * 30)
print(f'O jogador {jog["nome"]} jogou {len(jog["gols"])} partidas.')
for k, v in enumerate(gol):
    print(f'{"=> Na partida": >15} {k+1}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols.')

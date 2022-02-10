# DESAFIO 095
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes de aproveitamento de cada jogador.
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jog = dict()
geral = list()
gol = list()
while True:
    jog.clear()
    print('–' * 30)
    jog['nome'] = str(input('Nome do Jogador: ')).title()
    n = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    gol.clear()
    for c in range(1, n+1):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
    jog['gols'] = gol[:]
    jog['total'] = sum(gol)
    geral.append(jog.copy())
    while True:
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if av in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if av == "N":
        break
print('–=' * 30)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('–' * 40)
for k, v in enumerate(geral):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('–' * 40)
while True:
    q = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if q == 999:
        break
    if q >= len(geral):
        print(f'ERRO! Não existe jogador com código {q}')
    else:
        print(f' –– LEVANTAMENTO DO JOGADOR {geral[q]["nome"]}: ')
        for k, v in enumerate(geral[q]["gols"]):
            print(f'    No jogo {k+1} fez {v} gols')
    print('–' * 40)
print('<<< VOLTE SEMPRE >>>')

# DESAFIO 103
# Faça um programa que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.

def ficha(x='', g=''):
    if not x:
        x = '<desconhecido>'
    if not g.isnumeric():
        g = 0
    print(f'O jogador {x} fez {g} gol(s) no campeonato.')


ficha(str(input('Nome do jogador: ')).strip(), (str(input('Número de gols: '))).strip())

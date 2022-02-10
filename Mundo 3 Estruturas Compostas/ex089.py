# DESAFIO 089
# Crie um programa que leia nome e 2 notas de vários alunos e guarda tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

from time import sleep

alunos = []
while True:
    nome = str(input('Nome: ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
print('–=' * 22)
print(f'{"Nº":<3} {"NOME":<8} {"MÉDIA":>10}')
print('–' * 44)
for i, v in enumerate(alunos):
    print(f'{i:<4}{v[0]:<8}{v[2]:>9.1f}')
while True:
    print('–' * 44)
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    if num <= len(alunos) - 1:
        print(f'As notas de {alunos[num][0]} são {alunos[num][1]}')
print('<' * 3, 'VOLTE SEMPRE', '>' * 3)

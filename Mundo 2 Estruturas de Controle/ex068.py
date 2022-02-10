# DESAFIO 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador
# perder. Mostrando o total de vitórias consecutivas que ele conquistou no jogo.

from random import randint

cont = 0
print('=-' * 20)
print(f'{"VAMO JOGAR PAR OU ÍMPAR":^40}')
while True:
    print('=-' * 20)
    num = int(input('Digite um valor: '))
    comp = randint(1, 10)
    soma = num + comp
    pi = ' '
    while pi not in "PI":
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('–' * 40)
    print(f'Você jogou {num} e o computador {comp}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('–' * 40)
    if pi == "P":
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif pi == "I":
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=-' * 20)
print(f'GAME OVER! Você venceu {cont} vezes.')

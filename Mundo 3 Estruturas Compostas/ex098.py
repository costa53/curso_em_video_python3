# # DESAFIO 098
# Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo
# e realize a contagem. Seu programa tem que realizar 3 contagens através da função criada:
# A) de 1 até 10, de 1 em 1. B) de 10 até 0, de 2 em 2. C) Uma contagem personalizada.

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('—=' * 20)
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    sleep(1)
    if i > f:
        for v in range(i, f - 1, -p):
            print(v, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for v in range(i, f + 1, p):
            print(v, end=' ')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('—=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

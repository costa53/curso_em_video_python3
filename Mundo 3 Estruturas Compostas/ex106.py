# DESAFIO 106
# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar 'FIM', o programa se encerrará. OBS.: Use cores.

c = ('\033[m',      # — 0 resetar cor
     '\033[1;7m',   # — 1 negativo
     '\033[1;41m',  # — 2 back vermelho
     '\033[1;42m',  # — 3 back verde
     '\033[1;44m')  # — 4 back azul


def tit(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('–' * tam)
    print(f'  {msg}')
    print('–' * tam)
    print(c[0], end='')


def ajuda():
    from time import sleep
    while True:
        tit('SISTEMA DE AJUDA PyHELP', 3)
        x = input('Função ou Biblioteca > ').lower()
        if x != 'fim':
            tit(f"Acessando o manual do comando '{x}'", 4)
            sleep(1)
            print(c[1], end='')
            help(x)
            print(c[0], end='')
            sleep(1)
        else:
            break
    tit('FIM DO PROGRAMA!', 2)


ajuda()

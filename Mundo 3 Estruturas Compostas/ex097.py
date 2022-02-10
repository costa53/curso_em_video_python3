# DESAFIO 097
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adptável.

def escreva(txt):
    tam = len(txt) + 2
    print('~' * tam)
    print(f' {txt}')
    print('~' * tam)


escreva('Olá, Mundo')

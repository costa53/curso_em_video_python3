# DESAFIO 114
# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

from urllib import request, error

rc = "\033[m"
vermelho = "\033[1;31;40m"
amarelo = "\033[1;33;40m"

try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print(vermelho + f'O site Pudim não está acessível no momento.' + rc)
else:
    print(amarelo + 'Consegui acessar o site Pudim com sucesso!' + rc)
    print(site.read())

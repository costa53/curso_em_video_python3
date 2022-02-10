# DESAFIO 104
# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaint('Digite um n').

vermelho = "\033[0;31;40m"
rc = "\033[m"


def leiaint(x):
    while True:
        v = input(x).strip()
        if v.isnumeric():
            return v
        print(vermelho + 'ERRO! Digite um número inteiro válido.' + rc)


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

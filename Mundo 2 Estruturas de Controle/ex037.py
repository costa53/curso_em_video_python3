# DESAFIO 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('Bem vindo ao CONVERSOR')
dig = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
conv = int(input('Sua opção: '))
if conv == 1:
    bi = format(dig, 'b')
    print(f'O número {dig} convertido para binário é {bi}')
elif conv == 2:
    oc = format(dig, 'o')
    print(f'O número {dig} convertido para octal é {oc}')
elif conv == 3:
    he = format(dig, 'x')
    print(f'O número {dig} convertido para hexadecimal é {he}')
else:
    print('A opção digitada é inválida')

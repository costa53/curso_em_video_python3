# DESAFIO 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
av = ''
while av != "N":
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {ext[num]}')
    while True:
        av = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
        if av == "S" or av == "N":
            break
        elif av != "S":
            print('Tente novamente.', end=' ')
print('FIM')


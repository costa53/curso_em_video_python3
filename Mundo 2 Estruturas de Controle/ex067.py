# DESAFIO 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')

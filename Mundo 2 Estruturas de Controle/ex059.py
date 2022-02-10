# DESAFIO 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar; [2] multiplicar, [3] maior, [4] novos números; [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

opc = ''
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while opc != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opc = int(input('>>>>> Qual a sua opção? '))
    soma = v1 + v2
    mult = v1 * v2
    if opc == 1:
        print(f'A soma entre {v1} + {v2} é igual a {soma}')
    elif opc == 2:
        print(f'O resultado entre {v1} x {v2} é igual a {mult} ')
    elif opc == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor é {v1}')
        elif v2 > v1:
            print(f'Entre {v1} e {v2} o maior valor é {v2}')
        else:
            print(f'Os dois valores são iguais')
    elif opc == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente:')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

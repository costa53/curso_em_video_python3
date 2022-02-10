# DESAFIO 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.

valores = []
while True:
    num = int(input('Digite um valor: '))
    r = valores.count(num)
    if r == 0:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
valores.sort()
print(f'Você digitou os valores {valores}')

# DESAFIO 081
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores ordenada em forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

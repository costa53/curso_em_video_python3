# DESAFIO 075
# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

v = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {v}')
print(f'O valor 9 apareceu {v.count(9)} vezes')
if 3 in v:
    print(f'O valor 3 apareceu na {v.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: {p}' for p in v if p % 2 == 0)
#print('Os valores pares digitados foram:', ", ".join(f'{p}' for p in v if p % 2 == 0))

# DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper().replace(" ", "")
palindromo = frase[::-1]
print(f'O inverso de {frase} é {palindromo}')
if palindromo == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

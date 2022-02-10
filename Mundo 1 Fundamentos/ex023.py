# DESAFIO 023
# Faça um programa que leia um número de a 0 a 9999 e mostre na tela cada um dos digitos separados
# unidade, dezena, centena, milhar.

num = int(input('Digite um número de 0 a 9999: '))
n = str(num).zfill(4)
print(f'Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')

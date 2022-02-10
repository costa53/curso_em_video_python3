# DESAFIO 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo? ')).strip().upper().split()
print(f'Seu nome tem Silva? {"SILVA" in nome}')

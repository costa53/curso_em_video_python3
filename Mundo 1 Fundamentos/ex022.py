# DESAFIO 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas;
# Quantas letras ao total sem considerar espaços;
# Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo? ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome.replace(" ", ""))} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')

# DESAFIO 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo; Qual o nome do homem mais velho; Quantas mulheres tem menos de 21 anos.

soma = velho = cont = 0
nome2 = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        velho = idade
        nome2 = nome
    else:
        if idade > velho and sexo == 'M':
            velho = idade
            nome2 = nome
    if idade < 21 and sexo == 'F':
        cont += 1
m = soma / 4
print(f'A média de idade do grupo é de {m} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nome2}')
if cont == 0:
    print('Não tem mulheres com menos de 21 anos')
elif cont == 1:
    print('Ao todo tem 1 mulher com menos de 21 anos')
else:
    print(f'Ao todo tem {cont} mulheres com menos de 21 anos')

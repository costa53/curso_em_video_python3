# DESAFIO 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20.

total = hom = mul = 0
while True:
    print('–' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('–' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('–' * 30)
    if idade >= 18:
        total += 1
    if sexo == "F" and idade < 20:
        mul += 1
    if sexo == "M":
        hom += 1
    av = ' '
    while av not in "SN":
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if av == "N":
        break
print(f'{" FIM DO PROGRAMA ":=^29}')
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo tempos {hom} homens cadastrados')
print(f'E temos {mul} mulheres com menos de 20 anos')

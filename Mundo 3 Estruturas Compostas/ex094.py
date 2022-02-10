# DESAFIO 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas
# com idade acima da média.

dados = dict()
geral = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).title()
    while True:
        dados['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if dados['sexo'] in "MF":
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    geral.append(dados.copy())
    while True:
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if av in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if av == "N":
        break
print('–=' * 30)
print(geral)
print(f'A) O grupo tem {len(geral)} pessoas.')
media = soma / len(geral)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for i in geral:
    if i['sexo'] == "F":
        print(f'[{i["nome"]}] ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for i in geral:
    if i['idade'] > media:
        print()
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

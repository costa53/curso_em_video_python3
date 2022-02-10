# DESAFIO 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

av = ''
cont = soma = media = maior = menor = 0
while av in "Ss":
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while av not in "SsNn":
        print('Tente novamente.')
        av = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi de {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')

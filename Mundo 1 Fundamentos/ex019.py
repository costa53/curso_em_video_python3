# DESAFIO 019
# Um professor quer sortear um de deus 4 alunos para apagar a lousa. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
so = choice(lista)
print(f'O aluno escolhido foi: {so}')

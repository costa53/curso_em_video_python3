# DESAFIO 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('amanda', 'paulo', 'bijou', 'lolita', 'aprender', 'programar', 'linguagem', 'python',
            'estudar', 'futuro', 'praticar', 'programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for l in p:
        if l.lower() in "aeiou":
            print(l, end=' ')

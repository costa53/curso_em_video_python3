# DESAFIO 049
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

n1 = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{n1} x {c:2} = {n1 * c}')
print('-' * 12)

# DESAFIO 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

print('–' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('–' * 40)
p = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
     'Compasso', 9.99, 'Mochila', 120.30, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(p), 2):
    print(f'{p[c]:.<30}R${p[c+1]:7.2f}')
print('–' * 40)

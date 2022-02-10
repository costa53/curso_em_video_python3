# DESAFIO 010
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere U$1.00 = R$5.70.

r = float(input('Quantos reais você tem na carteira? R$'))
d = r / 5.70
print(f'Com R${r:.2f} você pode comprar US${d:.2f}')

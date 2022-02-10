# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule
# e mostre o comprimento da hipotenusa

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2) #  <— Outra opção é importar a função 'hypot' da biblioteca 'math'
print(f'O comprimento da hipotenusa é igual a {hi:.2f}')

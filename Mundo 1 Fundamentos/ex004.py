# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e 
# todas as informações possíveis sobre ela.

a = input('Diga alguma coisa: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

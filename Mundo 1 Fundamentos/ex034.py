# DESAFIO 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento;
# Para salários superiores a R$1.250,00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    novo = sal + (sal * 10) / 100
    print(f'Com aumento de 10%, seu novo salário é R${novo:.2f}')
else:
    novo = sal + (sal * 15) / 100
    print(f'Com aumento de 15%, seu novo salário é R${novo:.2f}')

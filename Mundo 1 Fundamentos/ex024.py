# DESAFIO 024
# Crie um programa que leia o nome de uma cidade e mostre se ela começa ou não com o nome "SANTO"

ci = str(input('Em que cidade você nasceu? ')).lstrip().upper()
print(ci[:5] == "SANTO" and ci[5] == " ")

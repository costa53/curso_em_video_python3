# DESAFIO 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# Abaixo de 18.5: ABAIXO DO PESO, entre 18.5 e 25: PESO IDEAL, 25 a 30: SOBREPESO
# 30 até 40: OBESIDADE, acima de 40: OBESIDADE MÓRBIDA.

peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual sua altura? (m) '))
imc = peso / (alt ** 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc < 25:
    print('Você está no PESO IDEAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')

# DESAFIO 040
# Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: Média abaixo de 5.0: REPROVADO, média entre 5.0 e 6.9: RECUPERAÇÃO e
# média 7.0 ou superior: APROVADO.

n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'A média do aluno foi de {m:.1f} e ele está REPROVADO!')
elif 7.0 > m >= 5.0:
    print(f'A média do aluno foi de {m:.1f} e ele está de RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi de {m:.1f} e ele foi APROVADO!')

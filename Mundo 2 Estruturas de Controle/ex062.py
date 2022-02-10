# DESAFIO 062
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('-=' * 15)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('-=' * 15)
num = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
pr = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(pr, end=' ➝ ')
        pr += rz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

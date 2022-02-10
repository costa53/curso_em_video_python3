# DESAFIO 061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

print('-=' * 15)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('-=' * 15)
num = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
pr = num
cont = 1
while cont <= 10:
    print(pr, end=' ➝ ')
    pr += rz
    cont += 1
print('FIM')

# DESAFIO 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostra os 10 primeiros
# termos dessa progressão.

print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
n1 = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
pr = 1
for c in range(0, 10):
    pr = n1 + (rz * c)
    print(pr, end=' ➝ ')
print('ACABOU')

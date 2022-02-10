# DESAFIO 080
# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
for i in range(0, 5):
    num = int(input('Digite um número: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for c in range(0, 5):
            if num <= valores[c]:
                valores.insert(c, num)
                print(f'Adicionado na posição {c} da lista...')
                break
print(f'Os valores digitados em ordem foram {valores}')

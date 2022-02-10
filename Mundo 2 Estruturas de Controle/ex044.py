# DESAFIO 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento: à vista dinheiro/ cheque: 10% de desconto; à vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.

print(f'{" LOJAS AMANDITA ":=^40}')
val = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))
if opc == 1:
    total = val - (val * 10 / 100)
    print(f'Sua compra de R${val:.2f} vai custar R${total:.2f} no final')
elif opc == 2:
    total = val - (val * 5 / 100)
    print(f'Sua compra de R${val:.2f} vai custar R${total:.2f} no final')
elif opc == 3:
    total = val
    mes = total / 2
    print(f'Sua compra será parcelada em 2x de R${mes:.2f} SEM JUROS.')
    print(f'Sua compra de R${val:.2f} vai custar R${total:.2f} no final')
elif opc == 4:
    total = val + (val * 20 / 100)
    pca = int(input('Quantas parcelas? '))
    mes = total / pca
    print(f'Sua compra será parcelada em {pca}x de R${mes:.2f} COM JUROS')
    print(f'Sua compra de R${val:.2f} vai custar R${total:.2f} no final')
else:
    print('Opção inválida de pagamento. Tente novamente!')

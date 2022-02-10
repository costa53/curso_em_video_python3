# DESAFIO 058
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('=' * 25)
print('JOGO DA ADIVINHAÇÃO V2.0')
print('=' * 25)
num = randint(0, 10)
cont = 0
adv = ''
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while adv != num:
    adv = int(input('Qual é seu palpite? '))
    if adv > 10:
        print('ERROU! É de 0 até 10. Tente de novo.')
    if adv > num and adv < 11:
        print('Menos... Tente mais uma vez.')
    if adv < num:
        print('Mais... Tenta mais uma vez.')
    cont += 1
if cont == 1:
    print('Nossa... Você acertou de primeira. Parabéns!')
else:
    print(f'Você acertou com {cont} tentativas. Parabéns!')

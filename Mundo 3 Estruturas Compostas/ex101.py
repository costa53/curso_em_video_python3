# DESAFIO 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO.

def voto(i):
    from datetime import date
    i = date.today().year - i
    if 18 <= i < 70:
        return f'Com {i} anos: VOTO OBRIGATÓRIO'
    elif 16 <= i < 18 or i >= 70:
        return f'Com {i} anos: VOTO OPCIONAL'
    else:
        return f'Com {i} anos: NÃO VOTA'


print(voto(int(input('Ano de Nascimento: '))))

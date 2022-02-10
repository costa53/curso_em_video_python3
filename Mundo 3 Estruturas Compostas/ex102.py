# DESAFIO 102
# Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo fatorial.

def fatorial(n, show):
    """
    —> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Retorna o valor de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))

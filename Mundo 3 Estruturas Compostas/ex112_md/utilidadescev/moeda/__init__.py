def aumentar(n=0, a=0, show=False):
    n += (n * a / 100)
    if show:
        return moeda(n)
    return n


def diminuir(n=0, b=0, show=False):
    n -= (n * b / 100)
    if show:
        return moeda(n)
    return n


def dobro(n=0, show=False):
    n *= 2
    if show:
        return moeda(n)
    return n


def metade(n=0, show=False):
    n /= 2
    if show:
        return moeda(n)
    return n


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, a=10, b=10):
    print('–' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('–' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{b}% de redução: \t{diminuir(n, b, True)}')
    print('–' * 30)

def aumentar(n=0, a=0, show=False):
    n += (n * a / 100)
    if show:
        return moeda(n)
    return n


def diminuir(n=0, a=0, show=False):
    n -= (n * a / 100)
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

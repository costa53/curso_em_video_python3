def aumentar(n=0, a=0):
    n += (n * a / 100)
    return n


def diminuir(n=0, a=0):
    n -= (n * a / 100)
    return n


def dobro(n=0):
    r = n * 2
    return r


def metade(n=0):
    r = n / 2
    return r


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

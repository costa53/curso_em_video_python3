vermelho = "\033[0;31;40m"
rc = "\033[m"


def leiadinheiro(x):
    while True:
        v = str(input(x).strip().replace(',', '.'))
        if not v.isalpha() and v != '':
            return float(v)
        print(vermelho + f"ERRO: '{v}' é um preço inválido!" + rc)

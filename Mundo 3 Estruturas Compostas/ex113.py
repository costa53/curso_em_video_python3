# DESAFIO 113
# Reescreva a função leiaint() que fizemos no DESAFIO 104, incluindo agora a possibilidade de digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

vermelho = "\033[0;31;40m"
rc = "\033[m"


def leiaint(x):
    while True:
        try:
            v = int(input(x))
        except KeyboardInterrupt:
            print(vermelho + '\nO usuário preferiu não digitar esse número.' + rc)
            return 0
        except (ValueError, TypeError):
            print(vermelho + 'ERRO! Digite um número inteiro válido.' + rc)
        else:
            return v


def leiafloat(x):
    while True:
        try:
            v = float(input(x).strip())
        except KeyboardInterrupt:
            print(vermelho + '\nO usuário preferiu não digitar esse número.' + rc)
            return 0
        except (ValueError, TypeError):
            print(vermelho + 'ERRO! Digite um número real válido.' + rc)
        else:
            return v


n = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')

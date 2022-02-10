rc = "\033[m"
negativo = "\033[7m"
vermelho = "\033[1;31;40m"
verde = "\033[1;32;40m"
amarelo = "\033[1;33;40m"
azul = "\033[1;34;40m"
magenta = "\033[1;35;40m"
ciano = "\033[1;36;40m"
cinza = '\033[1;37;40m'

from time import sleep


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


def tit(txt):
    print('–' * 42)
    print(txt.center(42))
    print('–' * 42)


def menu(lst):
    tit('MENU PRINCIPAL')
    c = 1
    for i in lst:
        print(amarelo + f'{c}' + rc, '–', azul + f'{i}' + rc)
        c += 1
    print('–' * 42)
    opc = leiaint(verde + 'Sua opção: ' + rc)
    return opc


def arqex(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        tit('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadast(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
        sleep(2)
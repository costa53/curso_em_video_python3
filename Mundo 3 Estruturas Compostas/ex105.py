# DESAFIO 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações: — Quantidade de notas; — Maior nota; — Menor nota;
# — Média da turma; – Situação (opcional).

def notas(*n, sit=False):
    """
    —> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não mostrar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


resp = notas(3.5, 8, 6.5, 8, 7, 9.5, sit=True)
print(resp)

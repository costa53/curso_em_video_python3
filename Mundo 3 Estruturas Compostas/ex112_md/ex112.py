# DESAFIO 112
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas
# as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.

from ex112_md.utilidadescev import moeda
from ex112_md.utilidadescev import dado

p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)

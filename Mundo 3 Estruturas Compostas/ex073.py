# DESAFIO 073
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre: A) apenas os 5 primeiros colocados. B) os 4 últimos colocados.
# C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR',
         'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {", ".join(times)}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {", ".join(times[:5])}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {", ".join(times[-4:])}')
print('-=' * 15)
print(f'Times em ordem alfabética: {", ".join(sorted(times))}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')

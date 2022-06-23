# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do campeonato brasileirão de futebol, na ordem de colocação.
# Depois mostre:
# [1] Apenas os 5 primeiros colocados.
# [2] Os últimos 4 colocados da tabela.
# [3] Uma lista com os times em ordem alfabética.
# [4] Em que posição na tabela está o time Fortaleza.

fortaleza = pos = 0
brasileirao = ('Palmeiras', 'Corinthians', 'Atlético-PR', 'Atlético-MG',
               'Internacional', 'Fluminense', 'Botafogo', 'antos', 'São Paulo',
               'Bragantino', 'Avaí', 'Atlético-GO', 'Ceará SC', 'Flamengo',
               'Coritiba', 'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')
for pos, time in enumerate(brasileirao):
    pos += 1
    print(f'O {time} está na {pos}ª posição')
    if time == 'Fortaleza':
        fortaleza = pos
print('-=' * 15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 15)
print(f'Os cinco primeiros são: {brasileirao[:5]}')
print('-=' * 15)
print(f'Os quatro últimos são: {brasileirao[-4:]}')
print('-=' * 15)
print(f'Os Fortaleza está na {fortaleza}ª posição')

# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO BRASILEIRÃO, NA ORDEM
# DE COLOCAÇÃO. DEPOIS MOSTRE:
# > APENAS OS 5 PRIMEIROS COLOCADOS
# > OS ULTIMOS 4 COLOCADOS
# > UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
# > EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE
t_brasileirao = ('Palmeiras SP', 'Corinthians SP', 'Fluminense RJ', 'Atletico Paranaense', 'CR Flamengo RJ', 'Internacional RS', 'Atletico Mineiro', 'Red Bull Bragantino SP', 'Santos FC SP', 'São Paulo FC SP', 'Goiás EC GO', 'Botafogo FR RJ', 'América FC MG', 'Ceará SC CE', 'Coritiba FC PR', 'Avaí FC SC', 'Cuiabá Esporte Clube MT', 'Fortaleza CE', 'Atletico Goianiense', 'EC Juventude RS')
print(f'Lista completa do Brasileirão {t_brasileirao}')
print(f'Os 5 primeiros são {t_brasileirao[:5]}')
print(f'Os 4 ultimos são {t_brasileirao[-4:]}')
print(f'Times em ordem alfabética {sorted(t_brasileirao)}')
print(f'O time Goiás está na {t_brasileirao.index("Goiás EC GO") + 1}° posição')

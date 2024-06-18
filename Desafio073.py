"""Este programa tem uma tupla com o nome dos vinte clubes da série A do campeonato
brasileiro. Ele mostra:
- Apenas os 5 primeiros colocados.
- Os últimos 4 colocados.
- Uma lista com os times em ordem alfabética.
- Em que posição o São Paulo está na tabela."""

brasileirao = (
    'Botafogo', 'Flamengo', 'Bahia', 'Athletico-PR',
    'São Paulo', 'Bragantino', 'Palmeiras', 'Cruzeiro',
    'Atlético-MG', 'Internacional', 'Juventude', 'Fortaleza',
    'Atlético-GO', 'Cuiabá', 'Vasco', 'Corinthians',
    'Grêmio', 'Criciúma', 'Fluminense', 'Vitória')

print('-' * 300)
print(f'Classificação do Brasileirão 2024: {brasileirao}')
print('-' * 300)
print(f'Os 5 primeiros são: {brasileirao[0:5]}')
print('-' * 300)
print(f'Os 4 últimos são: {brasileirao[16:]}')
print('-' * 300)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-' * 300)
print(f'O São Paulo está na: {brasileirao.index("São Paulo") + 1}ª posição.')

"""Este programa simula um jogo de dados com 4 jogadores, onde cada jogador
joga o dado uma vez. Os resultados dos lances de dados são guardados em um
dicionário. No final, ele mostra o valor que cada jogador tirou e mostra um
ranking do maior ao menor valor sorteado."""
from random import randint

lances_de_dados = {}

print('Valores sorteados:')
for i in range(1, 5):
    lances_de_dados[f'jogador{i}'] = randint(1, 6)

for k, v in lances_de_dados.items():
    print(f'O {k} tirou {v}')

lances_ordenados = dict(sorted(lances_de_dados.items(), key=lambda item: item[1], reverse=True))

posicao = 1

for k, v in lances_ordenados.items():
    print(f'{posicao}º lugar: {k} com {v}')
    posicao += 1

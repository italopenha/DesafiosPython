"""Este programa simula um jogo de dados com 4 jogadores, onde cada jogador
joga o dado uma vez. Os resultados dos lances de dados são guardados em um
dicionário. No final, ele mostra o valor que cada jogador tirou e mostra um
ranking do maior ao menor valor sorteado."""
from operator import itemgetter
from random import randint
from time import sleep

jogo = {}

print('Valores sorteados:')
for i in range(1, 5):
    jogo[f'jogador{i}'] = randint(1, 6)

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

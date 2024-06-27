"""Este programa pergunta ao usuário quantos jogos da Mega Sena ele quer
sortear. Depois, o programa sorteia a quantidade de jogos solicitada, cada jogo
tem 6 números diferentes entre 1 e 60."""
import time
from random import randint

n = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, end=' ')
print(f'SORTEANDO {n} JOGOS', end=' ')
print('-=' * 3)

for c in range(n):
    jogo = []
    while len(jogo) < 6:
        num_sorteado = randint(1, 60)
        if num_sorteado not in jogo:
            jogo.append(num_sorteado)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    time.sleep(1.5)

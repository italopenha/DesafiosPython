"""Este programa lê o nome de um jogador de futebol e quantas partidas
ele jogou. Depois ele lê a quantidade de gols feitos em cada partida.
No final, tudo isso é guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato."""

jogador = {}

jogador['nome'] = input('Nome do jogador: ')
partidas_jogadas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
jogador['gols'] = []

for i in range(partidas_jogadas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))

jogador['total_de_gols'] = sum(jogador['gols'])

print('-' * 100)
print(jogador)
print('-' * 100)
print(f'O campo nome tem o valor {jogador['nome']}.')
print(f'O campo gols tem o valor {jogador['gols']}.')
print(f'O campo total de gols tem o valor {jogador['total_de_gols']}.')
print('-' * 100)

print(f'O jogador {jogador['nome']} jogou {partidas_jogadas} partidas.')
for i in range(len(jogador['gols'])):
    print(f'   => Na partida {i + 1}, fez {jogador['gols'][i]} gols.')

print(f'Foi um total de {jogador['total_de_gols']} gols.')

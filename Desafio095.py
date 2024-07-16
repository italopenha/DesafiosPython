"""Este programa é um aprimoramento do desafio 93, agora ele lê os
dados de vários jogadores e inclui um sistema de visualização de
detalhes do aproveitamento de cada jogador."""

jogadores = []
jogador = dict()

while True:
    jogador.clear()
    print('-' * 100)
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['gols'] = []

    for i in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['total_de_gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())

    while True:
        opcao = input('Quer continuar? [S/N] ').lower().strip()
        if opcao != 's' and opcao != 'n':
            print('Erro! Digite apenas S ou N. Tente novamente.')
        else:
            break

    if opcao == 'n':
        break

print('cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 100)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    id_jogador = int(input('Mostrar os dados de qual jogador? (999 para parar). '))

    if id_jogador == 999:
        break

    if id_jogador < 0 or id_jogador >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {id_jogador}! Tente novamente.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[id_jogador]['nome']}:')
        for i in range(len(jogadores[id_jogador]['gols'])):
            print(f'    Na partida {i + 1}, fez {jogadores[id_jogador]['gols'][i]} gols.')

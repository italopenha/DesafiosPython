"""Este programa é um aprimoramento do desafio 93, agora ele lê os
dados de vários jogadores e inclui um sistema de visualização de
detalhes do aproveitamento de cada jogador."""

jogadores = []

while True:
    print('-' * 100)
    jogador = dict()
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas_jogadas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['gols'] = []

    for i in range(jogador['partidas_jogadas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['total_de_gols'] = sum(jogador['gols'])
    jogadores.append(jogador)

    opcao = input('Quer continuar? [S/N] ').lower().strip()
    if opcao == 'n':
        break

print('-' * 100)
print(f'{"Cód. ":<5}{"Nome":<10}{"Gols":<10}{"Total":<5}')
for i, j in enumerate(jogadores):
    print(f'{i:<5}{jogadores[i]['nome']:<10}{str(jogadores[i]['gols']):<10}{jogadores[i]['total_de_gols']:^5}')

while True:
    id_jogador = int(input('Mostrar os dados de qual jogador? (999) para parar. '))

    if id_jogador < 0 or id_jogador >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {id_jogador}! Tente novamente.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[id_jogador]['nome']}:')
        for i in range(len(jogadores[id_jogador]['gols'])):
            print(f'Na partida {i + 1}, fez {jogadores[id_jogador]['gols'][i]} gols.')

    if id_jogador == 999:
        break

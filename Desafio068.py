"""Este programa é um jogo de par ou ímpar. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo."""
import random

jogador_venceu = True
soma = 0
vitorias_consecutivas = 0

while jogador_venceu:
    escolha_jogador = input('Digite P para par ou I para ímpar: ').lower().strip()

    n_jogador = int(input('Escolha um número de 1 a 10: '))
    n_computador = random.randint(1, 10)
    soma = n_jogador + n_computador

    print('-' * 32)
    print(f'O computador escolheu o número {n_computador}')
    print(f'Você escolheu o número {n_jogador}')
    print(f'A soma entre esses valores é {soma}')
    print('-' * 32)

    if soma % 2 == 0:
        if escolha_jogador == 'p':
            jogador_venceu = True
            vitorias_consecutivas += 1
            print('Deu par, você venceu!')
        else:
            jogador_venceu = False
            print('Deu par, você perdeu!')
    else:
        if escolha_jogador == 'i':
            jogador_venceu = True
            vitorias_consecutivas += 1
            print('Deu ímpar, você venceu!')
        else:
            jogador_venceu = False
            print('Deu ímpar, você perdeu!')

print(f'Vitórias consecutivas: {vitorias_consecutivas}')



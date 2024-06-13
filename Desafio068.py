"""Este programa é um jogo de par ou ímpar. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo."""
import random

soma = 0
vitorias_consecutivas = 0

while True:
    n_jogador = int(input('Escolha um número de 1 a 10: '))
    n_computador = random.randint(0, 10)
    soma = n_jogador + n_computador
    escolha_jogador = ' '

    while escolha_jogador not in 'pi':
        escolha_jogador = input('Par ou ímpar? [P/I] ').lower()[0].strip()

    print('-' * 32)
    print(f'O computador escolheu o número {n_computador}')
    print(f'Você escolheu o número {n_jogador}')
    print(f'A soma entre esses valores é {soma}')
    print('-' * 32)

    if soma % 2 == 0:
        if escolha_jogador == 'p':
            vitorias_consecutivas += 1
            print('Deu par, você venceu!')
        else:
            print('Deu par, você perdeu!')
            break
    else:
        if escolha_jogador == 'i':
            vitorias_consecutivas += 1
            print('Deu ímpar, você venceu!')
        else:
            print('Deu ímpar, você perdeu!')
            break
    print('Vamos jogar navamente...')

print(f'Vitórias consecutivas: {vitorias_consecutivas}')

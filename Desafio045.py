# Este programa é um jogo de Jokenpô
import random
import time

minhaJogada = input('Digite: Pedra, Papel ou Tesoura ')

print('Gerando jogada...')
time.sleep(1.5)

jogadaPC = random.randrange(1, 4)
objetoPC = ''

if jogadaPC == 1:
    objetoPC = 'pedra'
elif jogadaPC == 2:
    objetoPC = 'papel'
else:
    objetoPC = 'tesoura'

print(30 * '*')
print(f'Escolha do computador: {objetoPC}')
print(f'Sua escolha: {minhaJogada}')
print(30 * '*')

if minhaJogada.lower() == 'pedra' and objetoPC == 'papel':
    print('O computador venceu!')
elif minhaJogada.lower() == 'pedra' and objetoPC == 'tesoura':
    print('Parabéns, você venceu!')
elif minhaJogada.lower() == 'papel' and objetoPC == 'tesoura':
    print('O computador venceu!')
elif minhaJogada.lower() == 'papel' and objetoPC == 'pedra':
    print('Parabéns, você venceu!')
elif minhaJogada.lower() == 'tesoura' and objetoPC == 'pedra':
    print('O computador venceu!')
elif minhaJogada.lower() == 'tesoura' and objetoPC == 'papel':
    print('Parabéns, você venceu!')
else:
    print(f'Empate!')
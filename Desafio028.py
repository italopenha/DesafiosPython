# Este programa gera um número inteiro aleatório entre 0 e 5 e pede para
# o usuário tentar acertar qual número é esse
import random

aleatorio = random.randrange(6)

n = int(input('Digite um número entre 0 e 5: '))

print(f'Número gerado: {aleatorio}')
print(f'Seu número: {n}')

if n == aleatorio:
    print('Você acertou!')
else:
    print('Você errou!') 
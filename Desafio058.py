# Este programa gera um número inteiro aleatório entre 0 e 10 e pede para
# o usuário tentar acertar qual número é esse. Caso o usuário erre, o programa
# continuará solicitando um novo número até o usuário acertar.
import random

aleatorio = random.randint(0, 10)
n = int
tentativas = 0
acertou = False

while not acertou:
    n = int(input('Digite um número entre 0 e 10: '))
    tentativas += 1

    if n == aleatorio:
        acertou = True
        print('--' * 10)
        print(f'Número sorteado: {aleatorio}')
        print('--' * 10)
        print(f'Acertou! Você precisou de {tentativas} tentativa(s) para acertar.')
    else:
        if n < aleatorio:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')


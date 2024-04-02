# Este programa lê um número inteiro e diz se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))

contador = 0

for c in range(1, n + 1):
    if n % c == 0:
        contador += 1

if contador == 2:
    print('É primo!')
else:
    print('Não é primo!')

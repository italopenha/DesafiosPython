# Este programa lê um número inteiro e mostra se ele é par ou ímpar.

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print(f'{n} é par.')
else:
    print(f'{n} é ímpar.')
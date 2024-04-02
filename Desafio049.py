# Este programa lê um número inteiro e mostra sua tabuada.

n = int(input('Digite um número inteiro: '))

for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
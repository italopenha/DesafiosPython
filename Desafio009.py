# Este programa lê um número inteiro qualquer e mostra na tela a sua tabuada.

n = int(input('Digite um número inteiro: '))

contador = 1;

print(f'Tabuada do {n}:')

while contador <= 10:
    print(f'{n} x {contador} = {n * contador}')
    contador += 1
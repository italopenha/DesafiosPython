"""Este programa gera 5 números aleatórios e os coloca em uma tupla.
Depois, ele mostra a listagem de números gerados e também indica o
menor e o maior valor."""
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

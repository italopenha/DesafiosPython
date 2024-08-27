"""Este programa tem a função maior(), que recebe vários parâmetros com valores inteiros.
Depois, ele analisa todos os valores e diz qual é o maior deles."""
from time import sleep

def maior(*num):
    maior = 0
    for n in num:
        print(n, end=' ')
        sleep(0.5)

        if maior == 0:
            maior = n
        elif n > maior:
            maior = n

    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
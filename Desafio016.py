# Este programa lê um número real qualquer e mostra a sua porção inteira.

import math

n = float(input('Digite um número real: '))
inteiro = math.trunc(n)

print(f'A porção inteira de {n} é igual a {inteiro}')
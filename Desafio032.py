# Este programa lê um ano qualquer e diz se ele é ou não bissexto.
from datetime import date

ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto.')
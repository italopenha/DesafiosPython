# Este programa lê um ano qualquer e diz se ele é ou não bissexto.

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto.')
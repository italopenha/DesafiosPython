"""Este programa lê 9 números inteiros e forma uma matriz de dimensão
3x3 com eles. No final, ele mostra a matriz na tela na formatação correta."""

matriz_3x3 = [[None, None, None], [None, None, None], [None, None, None]]

for l in range(3):
    for c in range(3):
        matriz_3x3[l][c] = int(input(f'Digite um valor para {l, c}: '))

for l in range(3):
    for c in range(3):
        print(f'[ {matriz_3x3[l][c]} ]', end='')
    print()

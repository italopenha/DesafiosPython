"""Este programa usa a base do Desafio086, mas agora acrescenta as seguintes
funcionalidades:
- Mostra a soma de todos os valores pares digitados.
- Mostra a soma dos valores da terceira coluna.
- Mostra o maior valor da segunda linha."""

matriz_3x3 = [[None, None, None], [None, None, None], [None, None, None]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
segunda_linha = []

for l in range(3):
    for c in range(3):
        matriz_3x3[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' * 100)

for l in range(3):
    for c in range(3):
        print(f'[{matriz_3x3[l][c]:^5}]', end='')

        if matriz_3x3[l][c] % 2 == 0:
            soma_pares += matriz_3x3[l][c]

        if c == 2:
            soma_terceira_coluna += matriz_3x3[l][c]

        if l == 1:
            segunda_linha.append(matriz_3x3[l][c])
    print()
maior_valor_segunda_linha = max(segunda_linha)

print('-' * 100)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}.')
print('-' * 100)

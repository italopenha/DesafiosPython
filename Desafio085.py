"""Este programa lê sete valores numéricos e os cadastra em uma única lista
que mantém separados os valores pares e ímpares. No final, ele mostra os
valores pares e ímpares em ordem crescente."""

numeros = [[], []]

for n in range(1, 8):
    numero = int(input(f'Digite o {n}º valor: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print('-' * 100)

print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')

"""Este programa lê vários números e os coloca em uma lista.
Depois, ele cria duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, ele mostra o conteúdo das três listas geradas."""

valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    opcao = input('Quer continuar? [S/N] ').strip().lower()

    if opcao == 'n':
        break

print('-' * 100)
print(f'A lista completa é {valores}')

pares = []
impares = []

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

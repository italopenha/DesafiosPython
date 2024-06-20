"""Este programa lê vários valores numéricos e cadastra-os em uma lista.
Caso o número já exista na lista, ele não será adicionado.
No final, serão exibidos todos os valores digitados, em ordem crescente."""

valores = list()

while True:
    n = int(input('Digite um valor: '))

    if n in valores:
        print(f'O valor {n} já está na lista! Não vou adicionar...')
    else:
        valores.append(n)
        print(f'Valor {n} adicionado com sucesso!')

    opcao = input('Quer continuar? [S/N] ').strip().lower()

    if opcao == 'n':
        break

print('-' * 100)
print(f'Você digitou os valores {sorted(valores)}')

"""Este programa lê 5 números e coloca-os em uma lista, já na posição
correta de inserção sem usar o sort(). No final ele mostra a lista ordenada."""

valores = list()

for i in range(0, 5):
    n = int(input('Digite um valor: '))

    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        if n < valores[0]:
            valores.insert(0, n)
            print('Adicionado na posição 0 da lista...')
        else:
            for j in range(0, len(valores) - 1):
                if n > valores[j] and n < valores[j + 1]:
                    valores.insert(j + 1, n)
                    print(f'Adicionado na posição {j + 1} da lista...')
                    break

print('-' * 60)
print(f'Os valores digitados na ordem foram {valores}')

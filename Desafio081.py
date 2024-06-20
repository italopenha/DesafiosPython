"""Este programa lê vários números e os coloca em uma lista.
Depois, ele mostra:
- Quantos números foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado ou não."""

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))

    opcao = input('Quer continuar? [S/N] ').strip().lower()

    if opcao == 'n':
        break

print('-' * 100)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')

if 5 in valores:
    print(f'O valor 5 foi encontrado na lista na posição {valores.index(5)}.')
else:
    print('O valor 5 não foi encontrado na lista.')
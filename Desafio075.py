"""Este programa lê 4 valores e guarda-os em uma tupla. No final, ele
mostra:
- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares."""

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

numeros = (a, b, c, d)
print(f'Você digitou os valores {numeros}')

if numeros.count(9) > 0:
    print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')
else:
    print(f'O valor 9 não foi digitado nenhuma vez.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')

cont_pares = 0

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        if cont_pares == 0:
            print('Os valores pares digitados foram:', end=' ')
        print(numeros[i], end=' ')
        cont_pares += 1

if cont_pares == 0:
    print('Nenhum número par foi digitado.')

"""Este programa lê o valor de 5 valores e guarda-os em uma lista.
No final, ele mostra qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista."""

valores = list()

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

print(f'Você digitou os valores: {valores}')

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(f'{i}...', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if valores[i] == menor:
        print(f'{i}...', end=' ')

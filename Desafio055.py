# Este programa lê o peso de cinco pessoas. No final ele mostra qual foi o maior e menor peso.

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))

    if peso > maior:
        maior = peso
        if c == 0:
            menor = peso
    elif peso < menor:
        menor = peso

print(f'Maior: {maior}')
print(f'Menor: {menor}')

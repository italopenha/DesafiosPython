# Este programa lê três números e mostra qual deles é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3
elif n3 > n1 and n3 > n2:
    maior = n3
    if n2 < n1:
        menor = n2
    else:
        menor = n1

print(f'Maior: {maior}')
print(f'Menor: {menor}')
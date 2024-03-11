# Este programa lê um valor em reais e converte para dólar.

cotacaoDolar = 4.97

reais = float(input('Digite um valor em reais: '))

dolares = reais / cotacaoDolar

print(f'{reais} é igual a {dolares:.2f} dólares')
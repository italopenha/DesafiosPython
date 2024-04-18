'''Este programa lê um número qualquer e mostra seu fatorial.'''

n = int(input('Digite um número para descobrir seu fatorial: '))
inicial = n
fim = n
fatorial = int

if n == 0 or n == 1:
    fatorial = 1
    fim = 1

'''while fim != 1:
    fim -= 1
    fatorial = n * fim
    n = fatorial'''

for i in range(n - 1, 1, -1):
    fatorial = n * i
    n = fatorial

print(f'{inicial}! = {fatorial}')

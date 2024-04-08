# Este programa lê seis númeors inteiros e mostra a soma apenas daqueles
# que são pares. Se o valor digitado for ímpar, ele é desconsiderado.

soma_pares = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma_pares += n

print(f'A soma dos pares é {soma_pares}.')
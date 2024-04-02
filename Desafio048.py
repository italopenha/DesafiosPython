# Este programa calcula a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo entre 1 até 500.

soma_impares = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma_impares += c


print(soma_impares)
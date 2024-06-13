"""Este programa lê vários números inteiros e só para quando o usuário
digitar o valor 999, que é a condição de parada. No final, ele mostra
quantos números foram digitados e qual a soma entre eles(desconsidernado o 999)."""

n = 0
numeros_digitados = 0
soma = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))

    if n == 999:
        break

    numeros_digitados += 1
    soma += n

print(f'Números digitados: {numeros_digitados}')
print(f'Soma entre eles: {soma}')

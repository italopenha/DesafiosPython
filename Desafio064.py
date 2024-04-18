"""Este programa lê vários números inteiros, e só para quando o usuário
digita o valor 999. No final, ele mostra quantos números foram digitados
e qual foi a soma entre eles, desconsiderando a flag de parada 999."""

n = contador = soma = 0

while n != 999:
    n = int(input('Digite um número inteiro qualquer ou 999 para parar: '))

    if n != 999:
        soma += n
        contador += 1

print(f'Foram digitados {contador} números.')
print(f'A soma entre eles é {soma}')

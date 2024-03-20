# Este programa lê um salário e calcula o valor do seu aumento.

salarioAtual = float(input('Digite o seu salário: '))

salarioNovo = 0

if salarioAtual > 1250.00:
    salarioNovo = salarioAtual * 0.10 + salarioAtual
else:
    salarioNovo = salarioAtual * 0.15 + salarioAtual

print(f'Seu novo salário é R$ {salarioNovo:.2f}')
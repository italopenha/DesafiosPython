# Este programa verifica se uma pessoa pode pedir um empréstimo bancário
# para comprar uma casa. O empréstimo será aprovado se o valor da prestação mensal
# não ultrapassar 30% do salário.

valorDaCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você quer pagar? '))

trintaPorCentoDoSalario = salario * 0.3
qtdParcelas = anos * 12
valorParcelas = valorDaCasa / qtdParcelas

if valorParcelas > trintaPorCentoDoSalario:
    print(f'Com esses valores, você deveria pagar {qtdParcelas} parcelas de R$ {valorParcelas:.2f}, e isso ultrapassaria 30% do seu salário que é {trintaPorCentoDoSalario:.2f}.')
    print('Empréstimo negado!')
else:
    print(f'Com esses valores, você deveria pagar {qtdParcelas} parcelas de R$ {valorParcelas:.2f}, e isso está dentro de 30% do seu salário que é {trintaPorCentoDoSalario:.2f}.')
    print('Empréstimo aprovado!')
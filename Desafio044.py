# Este programa calcula o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento.

precoInicial = float(input('Digite o preço do produto: '))
print(31 * '-')
print('''Escolha a condição de pagamento:
Digite [1] para à vista no dinheiro/cheque
Digite [2] para à vista no cartão
Digite [3] para em até 2x no cartão
Digite [4] para até 3x ou mais no cartão''')

formaPagamento = input()
print(31 * '-')

if formaPagamento == '1':
    precoFinal = precoInicial - precoInicial * 0.10
    print(f'À vista no dinheiro ou cheque você terá que pagar R$ {precoFinal:.2f}.')
elif formaPagamento == '2':
    precoFinal = precoInicial - precoInicial * 0.05
    print(f'À vista no cartão você terá que pagar R$ {precoFinal:.2f}.')
elif formaPagamento == '3':
    parcelas = precoInicial / 2
    print(f'Você terá que pagar R$ {precoInicial:.2f} em duas parcelas de R$ {parcelas:.2f}.')
elif formaPagamento == '4':
    precoFinal = precoInicial + precoInicial * 0.20

    qtdParcelas = 0
    while qtdParcelas < 3:
        qtdParcelas = int(input('Em quantas parcelas você quer pagar? Mínimo 3.'))
        if qtdParcelas < 3:
            print('Quantidade de parcelas deve ser 3 ou mais!')

    parcelas = precoFinal / qtdParcelas
    print(f'Você terá que pagar R$ {precoFinal:.2f} em {qtdParcelas} parcelas de R$ {parcelas:.2f}.')
else:
    print('Opção inválida.')
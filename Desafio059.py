# Este programa lê dois valores e mostra um menu na tela indicando qual
# operação o usuário deseja realizar com aqueles dois números.
from time import sleep

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = int

while opcao != 5:
    print('-' * 18)
    print('Escolha uma opção:')
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Maior ou igual\n[4] - Novos números\n[5] - Sair do programa')
    opcao = int(input())

    if opcao == 1:
        print(f'SOMA: {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'MULTIPLICAÇÃO: {n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'MAIOR OU IGUAL: {n1} é maior que {n2}')
        elif n2 > n1:
            print(f'MAIOR OU IGUAL: {n2} é maior que {n1}')
        else:
            print(f'MAIOR OU IGUAL: {n1} é igual a {n2}')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        break
    else:
        print('Opção inválida. Tente Novamente.')
    sleep(2)
    
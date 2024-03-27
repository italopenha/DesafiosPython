# Este programa lê um número inteiro qualquer e o converte para outra base
# numérica escolhida pelo usuário, que pode ser binário, octal ou hexadecimal.

n = int(input('Digite um número inteiro: '))
base = input('Digite B para converter para binário, O para octal ou H para hexadecimal: ')

if base.lower() == 'b':
    print(f'{n} em binário é {bin(n)[2:]}')
elif base.lower() == 'o':
    print(f'{n} em octal é {oct(n)[2:]}')
elif base.lower() == 'h':
    print(f'{n} em hexadecimal é {hex(n)[2:]}')
else:
    print('Operação inválida!')
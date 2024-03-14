# Este programa lê um número inteiro de 0 a 9999 e mostra na tela
# cada um dos dígitos separados.

n = input('Digite um número inteiro entre 0 e 9999: ')

if len(n) == 4:
    print(f'Unidade: {n[-1]}')
    print(f'Dezena: {n[-2]}')
    print(f'Centena: {n[-3]}')
    print(f'Milhar: {n[-4]}')
elif len(n) == 3:
    print(f'Unidade: {n[-1]}')
    print(f'Dezena: {n[-2]}')
    print(f'Centena: {n[-3]}')
elif len(n) == 2:
    print(f'Unidade: {n[-1]}')
    print(f'Dezena: {n[-2]}')
elif len(n) == 1:
    print(f'Unidade: {n[-1]}')
else:
    print('Erro. O número digitado não está entre 0 e 9999')
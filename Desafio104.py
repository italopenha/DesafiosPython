'''Este programa tem uma função chamada leiaInt que funciona semelhante ao comando input,
só que fazendo a validação para aceitar apenas um valor numérico inteiro.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')
            continue

    return n

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')




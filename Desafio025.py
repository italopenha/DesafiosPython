# Este programa lê o nome de uma pessoa e verifica se ela tem "Silva" no nome.

nome = input('Digite um nome completo: ')

if nome.lower().count('silva', 0) > 0:
    print('Tem Silva')
else:
    print('Não tem Silva')
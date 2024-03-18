# Este programa lê o nome de uma pessoa e verifica se ela tem "Silva" no nome.

nome = input('Digite um nome completo: ').strip()

if 'silva' in nome.lower():
    print('Tem Silva')
else:
    print('Não tem Silva')
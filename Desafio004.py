# Este programa lê algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input('Digite algo: ')

print(f'É do tipo: {type(variavel)}')
print(f'É uma letra? {variavel.isalpha()}')
print(f'É número? {variavel.isnumeric()}')
print(f'É alfanumérico? {variavel.isalnum()}')
print(f'É um dígito? {variavel.isdigit()}')
print(f'É minúsculo? {variavel.islower()}')
print(f'É maiúsculo? {variavel.isupper()}')

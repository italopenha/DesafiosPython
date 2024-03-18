# Este programa lê o nome de uma cidade e diz se ela começa ou não
# com o nome "Santo"

nome = input('Digite o nome de uma cidade: ').strip()

if nome[:5].lower() == 'santo':
    print('Esse nome começa com a palavra "Santo"')
else:
    print('Esse nome não começa com a palavra "Santo"')
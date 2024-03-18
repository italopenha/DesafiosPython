# Este programa lê uma frase, e em seguida mostra a primeira e a última palavra.

frase = input('Digite uma frase: ').strip()

lista_de_palavras = frase.split()

primeira_palavra = lista_de_palavras[0]
ultima_palavra = lista_de_palavras[-1]

print(f'Primeira palavra: {primeira_palavra}')
print(f'Última palavra: {ultima_palavra}')
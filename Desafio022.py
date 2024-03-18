# Este programa lê uma frase e mostra na tela essa frase nas seguintes condições:
# Com todas as letras maiúsculas
# Com todas as letras minúsculas
# Quantas letras ela tem (sem considerar espaços)
# Quantas letras tem a primeira palavra

frase = input('Digite uma frase: ').strip()

print(f'Só em maiúsculas: {frase.upper()}')
print(f'Só em minúsculas: {frase.lower()}')

lista_de_palavras = frase.split()
frase_sem_espacos = ''.join(lista_de_palavras)

print(f'Quantas letras a frase tem ao todo: {len(frase_sem_espacos)}')
print(f'Quantas letras tem a primeira palavra: {len(lista_de_palavras[0])}')
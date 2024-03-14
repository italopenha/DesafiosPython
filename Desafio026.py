# Este programa lê uma frase e mostra:
# Quantas vezes aparece a letra A
# Em que posição a letra A aparece pela primeira vez
# Em que posição a letra A aparece pela última vez

frase = input('Digite uma frase: ')

quantidade_de_a = frase.lower().count('a')

posicao_do_primeiro_a = frase.lower().find('a')

posicao_do_ultimo_a = frase.lower().rfind('a')

print(f'Quantas vezes aparece a letra A: {quantidade_de_a}')
print(f'Em que posição a letra A aparece pela primeira vez: {posicao_do_primeiro_a}')
print(f'Em que posição a letra A aparece pela última vez {posicao_do_ultimo_a}')

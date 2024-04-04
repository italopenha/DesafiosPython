# Este programa lê uma frase e verifica se ela é um palíndromo.

frase = input('Digite uma frase: ')

frase_formatada = frase.lower().replace(' ', '')
frase_lista = list(frase_formatada)
contador = -1

for c in range(0, len(frase_lista) // 2):
    frase_lista[c], frase_lista[contador] = frase_lista[contador], frase_lista[c]
    contador -= 1

frase_ao_contrario = ''.join(frase_lista)

e_palindromo = False

for c in range(0, len(frase_formatada)):
    if frase_formatada[c] == frase_ao_contrario[c]:
        e_palindromo = True
        contador -= 1
    else:
        e_palindromo = False
        break

if e_palindromo:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
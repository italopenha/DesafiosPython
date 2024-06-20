"""Este programa lê uma expressão matemática qualquer que usa parênteses.
E depois, valida se a expressão passada está com os parênteses abertos e
fechados na ordem correta."""

expressao = input('Digite sua expressão: ')

caracteres = []

for e in expressao:
    caracteres.append(e)

n_parenteses_direita = caracteres.count('(')
n_parenteses_esquerda = caracteres.count(')')

if n_parenteses_direita == n_parenteses_esquerda:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')

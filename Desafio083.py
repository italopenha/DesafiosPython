"""Este programa lê uma expressão matemática qualquer que usa parênteses.
E depois, valida se a expressão passada está com os parênteses abertos e
fechados na ordem correta."""

expressao = input('Digite sua expressão: ')

pilha = []

for e in expressao:
    if e == '(':
        pilha.append('(')
    elif e == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')

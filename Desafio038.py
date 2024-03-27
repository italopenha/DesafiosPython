# Este programa lê um número inteiro e mostra na tela qual é o maior
# ou se são iguais.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}!')
elif n2 > n1:
    print(f'{n2} é maior que {n1}!')
else:
    print('São iguais!')


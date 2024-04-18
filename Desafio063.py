'''Este programa lê um número inteiro n e mostra na tela os n primeiros
elementos de uma sequência de Fibonacci.'''

n = 0
print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))

while n == 0:
    print('Digite um número maior do que zero!')
    n = int(input('Quantos termos da sequência de Fibonacci? '))

t1 = 0
t2 = 1
t3 = t1 + t2
contador = 3

if n == 1:
    print(t1)
elif n == 2:
    print(f'{t1} - {t2}')
elif n == 3:
    print(f'{t1} - {t2} - {t3}')
else:
    print(f'{t1} - {t2} - {t3}', end=' - ')

    while contador < n:
        t1, t2 = t2, t3
        t3 = t1 + t2

        if contador == n - 1:
            print(t3)
        else:
            print(t3, end=' - ')

        contador += 1

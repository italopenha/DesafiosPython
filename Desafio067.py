"""Este programa lê números e mostra suas respectivas tabuada. Ele para
quando o usuário digitar um valor negativo."""

n = 1

while n >= 0:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? Digite um valor negativo para encerrar. '))
    print('-' * 30)

    if n >= 0:
        while cont <= 10:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1

        print('-' * 30)

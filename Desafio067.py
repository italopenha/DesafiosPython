"""Este programa lê um número e mostra suas respectiva tabuada, e depois
 pergunta ao usuário se ele quer ver outra tabuada. Ele para
quando o usuário digitar um valor negativo."""

while True:
    n = int(input('Quer ver a tabuada de qual valor? Digite um valor negativo para encerrar. '))

    if n < 0:
        break

    print('-' * 30)
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)

"""Este programa tem uma função chamada contador(), que recebe três parâmetros: início, fim e
passo e realiza a contagem."""

def contagem(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1

    print('-=' * 50)
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if i > f:
        for n in range(i, f - 1, p * -1):
            print(n, end=' ')
    else:
        for n in range(i, f + 1, p):
            print(n, end=' ')
    print('FIM!')
    print('-=' * 50)

contagem(1, 10, 1)
contagem(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contagem(inicio, fim, passo)
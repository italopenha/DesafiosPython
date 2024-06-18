"""Este programa lê um número entre 0 e 20 digitado pelo usuário e mostra
esse número por extenso."""

numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze',
    'catorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = ''

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    while n not in range(0, 21):
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    for numero in range(0, len(numeros_por_extenso)):
        if n == numero:
            print(f'Você digitou o número {numeros_por_extenso[numero]}.')
            continuar = input('Quer continuar? [S/N] ').strip().lower()

    if continuar == 'n':
        break

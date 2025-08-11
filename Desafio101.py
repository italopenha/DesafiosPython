'''Este programa calcula a idade de uma pessoa e mostra na tela se ela deve votar ou não. '''

from datetime import date

def voto(ano):
    idade = date.today().year - ano

    msg = ''

    if idade >= 18 and idade <= 65:
        msg = 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        msg = 'NÃO VOTA'
    else:
        msg = 'VOTO OPCIONAL'

    msgCompleta = f'Com {idade} anos: {msg}.'

    return msgCompleta

while True:
    try:
        ano = int(input('Digite seu ano de nascimento: '))

        if ano > date.today().year:
            print('Ano inválido. Tente novamente.')
        else:
            break
    except ValueError:
        print('Entrada inválida. Tente novamente.')

print(voto(ano))
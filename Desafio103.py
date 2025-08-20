'''Este programa tem uma função chamada ficha(), que recebe dois parâmetros opcionais:
o nome do jogador e quantos gols ele marcou.
Depois, o programa mostra a ficha do jogador, mesmo que algum dado não tenha sido informado.'''

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'

    if gols == '':
        gols = 0

    return f'O jogador {nome} fez {gols} gols(s) no campeonato.'

nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')

print(ficha(nome, gols))
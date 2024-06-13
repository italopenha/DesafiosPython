"""Este programa lê o sexo e a idade de várias pessoas. A cada pessoa cadastrada,
o programa pergunta se o usuário quer ou não continuar, e no final ele mostra:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem mais de 20 anos."""

pessoas_maiores_de_18 = 0
homens = 0
mulheres_maiores_de_20 = 0

while True:
    sexo = str
    resposta = str

    print('-' * 19)
    print('Cadastre uma pessoa')
    print('-' * 19)
    idade = int(input('Idade: '))

    while sexo != 'm' and sexo != 'f':
        sexo = input('Sexo: [M/F] ').lower()[0].strip()

    if idade > 18:
        pessoas_maiores_de_18 += 1

    if sexo == 'm':
        homens += 1

    if idade > 20 and sexo == 'f':
        mulheres_maiores_de_20 += 1

    while resposta != 's' and resposta != 'n':
        resposta = input('Quer continuar? [S/N] ').lower()[0].strip()

    if resposta == 'n':
        break

print('-' * 30)
print(f'{pessoas_maiores_de_18} pessoa(s) tem mais de 18 anos.')
print(f'Temos {homens} homem(ns).')
print(f'Temos {mulheres_maiores_de_20} mulher(es) com mais de 20 anos.')
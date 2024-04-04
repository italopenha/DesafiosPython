# Este programa lê o nome, idade e sexo de 4 pessoas e no final mostra:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

media = 0.0
idade = 0
soma_idades = 0
mais_velho = ''
maior = 0
mulheres_menores_20 = 0

for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [m] ou [f]: ')

    soma_idades += idade

    if idade > maior:
        maior = idade
        mais_velho = nome

    if sexo.lower() == 'f':
        if idade < 20:
            mulheres_menores_20 += 1


media = soma_idades / 4

print(f'A média de idade desse grupo é de {media} anos.')
print(f'O mais velho(a) é {mais_velho}, com {maior} anos.')

if mulheres_menores_20 > 0:
    print(f'Temos {mulheres_menores_20} mulher(es) com menos de 20 anos.')


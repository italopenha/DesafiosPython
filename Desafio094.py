"""Este programa lê nome, sexo e idade de várias pessoas e coloca os
dados da cada uma delas em um dicionário, e todas as pessoas em uma lista.
No final, ele mostra:
- Quantas pessoas foram cadastradas
- A média de idade do grupo
- Uma lista com todas as mulheres
- Uma lista com todas as pessoas com idade acima da média"""

pessoas = []
soma_idades = 0

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').lower().strip()
        if pessoa['sexo'] != 'f' and pessoa['sexo'] != 'm':
            print('Opção inválida, digite M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']

    pessoas.append(pessoa)

    while True:
        opcao = input('Quer continuar? [S/N] ').lower().strip()
        if opcao != 's' and opcao != 'n':
            print('Erro! Digite apenas S ou N. Tente novamente.')
        else:
            break

    if opcao == 'n':
        break

media_idades = soma_idades / len(pessoas)

print('-' * 100)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media_idades:5.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for i in range(len(pessoas)):
    if pessoas[i]['sexo'] == 'f':
        print(pessoas[i]['nome'], end=' ')

print(f'\n- Lista das pessoas que estão acima da média de idade:')
for p in pessoas:
    if p['idade'] > media_idades:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<<< ENCERRADO >>>')

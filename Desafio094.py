"""Este programa lê nome, sexo e idade de várias pessoas e coloca os
dados da cada uma delas em um dicionário, e todas as pessoas em uma lista.
No final, ele mostra:
- Quantas pessoas foram cadastradas
- A média de idade do grupo
- Uma lista com todas as mulheres
- Uma lista com todas as pessoas com idade acima da média"""

pessoas = []

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').lower().strip()
    while pessoa['sexo'] != 'f' and pessoa['sexo'] != 'm':
        print('Opção inválida, digite M ou F.')
        pessoa['sexo'] = input('Sexo: [M/F] ').lower().strip()
    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa)

    opcao = input('Quer continuar? [S/N] ').lower().strip()
    if opcao == 'n':
        break

soma_idades = 0
for i in range(len(pessoas)):
    soma_idades += pessoas[i]['idade']

media_idades = soma_idades / len(pessoas)

print('-' * 100)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media_idades} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for i in range(len(pessoas)):
    if pessoas[i]['sexo'] == 'f':
        print(pessoas[i]['nome'], end=' ')

print(f'\n- Lista das pessoas que estão acima da média de idade:')
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media_idades:
        print(f'nome = {pessoas[i]['nome']}; sexo = {pessoas[i]['sexo']}; idade = {pessoas[i]['idade']};')

print('<<< ENCERRADO >>>')

"""Este programa lê o nome e peso de várias pessoas, guardando tudo em
uma lista. No final, ele mostra:
- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas com mais pesadas.
- Uma listagem com as pessoas mais leves."""

quantidade_pessoas = 0
dado = list()
pessoas = list()
maior_peso = float
menor_peso = float
pessoas_mais_pesadas = list()
pessoas_mais_leves = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dado.append(nome)
    dado.append(peso)
    pessoas.append(dado[:])
    dado.clear()

    quantidade_pessoas += 1

    opcao = str(input('Quer continuar? ')).strip().lower()

    if opcao == 'n':
        break

for i in range(0, len(pessoas)):
    if i == 0 or pessoas[i][1] <= menor_peso:
        menor_peso = pessoas[i][1]

    if i == 0 or pessoas[i][1] >= maior_peso:
        maior_peso = pessoas[i][1]

for i in range(0, len(pessoas)):
    if pessoas[i][1] == menor_peso:
        pessoas_mais_leves.append(pessoas[i][0])

    if pessoas[i][1] == maior_peso:
        pessoas_mais_pesadas.append(pessoas[i][0])

print('-' * 100)
print(f'Ao todo, você cadastrou {quantidade_pessoas} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoas_mais_pesadas}')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {pessoas_mais_leves}')

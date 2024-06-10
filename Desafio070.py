"""Este programa lê o nome e o preço de vários produtos. E depois pergunta se o usuário
quer continuar, no final ele mostra:
- O total gasto na compra.
- Quantos produtos tem mais de R$ 1000,00.
- Qual é o nome do produto mais barato."""

total_gasto = 0
produtos_maiores_1000 = 0
produto_mais_barato = str
preco_mais_barato = 0
continuar = True
contador = 0

while continuar:
    resposta = str
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))

    if preco > 1000.00:
        produtos_maiores_1000 += 1

    if contador == 0:
        produto_mais_barato = nome
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            produto_mais_barato = nome

    contador += 1
    total_gasto += preco

    while resposta != 's' and resposta != 'n':
        resposta = input('Quer continuar? [S/N] ')

    if resposta == 'n':
        continuar = False

print('*** FIM DO PROGRAMA ***')
print(f'Valor total gasto: R$ {total_gasto:.2f}')
print(f'Total de produtos com preço maior que R$ 1000,00: {produtos_maiores_1000}')
print(f'Nome do produto mais barato: {produto_mais_barato}')



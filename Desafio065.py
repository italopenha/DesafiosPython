"""Este lê vários números inteiros e pergunta ao usuário se ele quer continuar
ou não. No final, ele mostra a média entre todos os números e qual foi o maior
e o menor valor."""

opcao = str
soma = media = maior = menor = quantidade = 0

while opcao != 'n':
    n = int(input('Digite um número inteiro: '))

    if n > maior:
        maior = n
        if quantidade == 0:
            menor = n
    elif n < menor:
        menor = n

    soma += n
    quantidade += 1
    opcao = input('Quer continuar? [S/N]').lower().strip()

media = soma / quantidade
print(f'Você digitou {quantidade} número(s).')
print(f'Média dos números digitados: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')

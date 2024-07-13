"""Este programa lê o nome, ano de nascimento e carteira de trabalho
e os cadastra(com idade) em um dicionário, se a CTPS for diferente de 0,
o dicionário receberá também o ano de contratação e o salário. Depois,
ele calcula a idade da pessoa e com quantos anos ela vai se aposentar
considerando o tempo de contribuição de 35 anos."""
from datetime import date

pessoa = dict()
pessoa['nome'] = input('Nome: ')
ano_de_nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano_de_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (Digite 0 se não tiver): '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['contratação'] - ano_de_nascimento + 35

print('-' * 100)
print(pessoa)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

"""Este programa lê o nome e média de notas de um aluno e processa se ele está aprovado ou reprovado,
guardando esses valores em um dicionário. No final, ele mostra o conteúdo da
estrutura na tela."""

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['média']}')
print(f'Situação é igual a {aluno['situação']}')

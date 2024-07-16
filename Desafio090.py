"""Este programa lê o nome e média de notas de um aluno e processa se ele está aprovado ou reprovado,
guardando esses valores em um dicionário. No final, ele mostra o conteúdo da
estrutura na tela."""

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-' * 50)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

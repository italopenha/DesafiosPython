"""Este programa lê o nome e duas notas de vários alunos e guarda tudo
em uma lista composta. No final, ele mostra um boletim contendo a média
de cada aluno e permite que o usuário possa mostrar as notas de cada aluno
individualmente."""

alunos = []
medias = []

while True:
    aluno = list()
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    alunos.append(aluno[:])
    media = (aluno[1] + aluno[2]) / 2
    medias.append(media)

    opcao = str(input('Quer continuar? [S/N] ')).strip().lower()
    if opcao == 'n':
        break

print('-=' * 50)
print(f'No. Nome Média')
print('-' * 50)

for i, a in enumerate(alunos):
    print(f'{i}   {alunos[i][0]} {medias[i]:.1f}')

while True:
    print('-' * 50)
    i = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))

    if i == 999:
        break

    print(f'Notas de {alunos[i][0]} são [{alunos[i][1]}, {alunos[i][2]}]')

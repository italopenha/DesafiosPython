def notas(*notas, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas do aluno
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre o aluno
    """
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    soma = sum(notas)
    media = sum(notas) / len(notas)
    situacao = ''

    if sit == True:
        if media < 5:
            situacao = 'Ruim'
        elif media >= 5 and media < 7:
            situacao = 'Razoável'
        elif media >= 7 and media < 10:
            situacao = 'Boa'
        else:
            situacao = 'Perfeita'

        return {'total': total, 'maior': maior, 'menor': menor, 'média': soma / total, 'situacao': situacao}
    else:
        return {'total': total, 'maior': maior, 'menor': menor, 'média': soma / total}


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)




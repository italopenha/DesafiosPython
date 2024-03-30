# Este programa lê o ano de nascimento de um jovem e informa de acordo com
# sua idade se ele ainda vai se alistar ao serviço militar, se já é hora de se alistar
# ou se já passou da hora. Além do tempo que falta no caso de ainda não ter chegado a hora.
import datetime

genero = input('Você é homem ou mulher? Digite H para homem ou M para mulher: ')

if genero.lower() == 'h':
    anoDeNascimento = int(input('Digite o seu ano de nascimento: '))

    anoAtual = datetime.datetime.now().year
    idade =  anoAtual - anoDeNascimento

    print(f'Quem nasceu em {anoDeNascimento} tem {idade} anos em {anoAtual}.')
    if idade > 18:
        print(f'Seu alistamento foi a {idade - 18} anos atrás, em {anoAtual - (idade - 18)}.')
    elif idade < 18:
        print(f'Faltam {18 - idade} anos para você chegar a idade de alistamento, será em {anoAtual + (18 - idade)}.')
    else:
        print(f'Você deve se alistar esse ano!')
elif genero.lower() == 'm':
    print('Mulheres não precisam se alistar no Brasil.')
else:
    print('Opção inválida!')

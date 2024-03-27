# Este programa lê o ano de nascimento de um jovem e informa de acordo com
# sua idade se ele ainda vai se alistar ao serviço militar, se já é hora de se alistar
# ou se já passou da hora. Além do tempo que falta no caso de ainda não ter chegado a hora.
import datetime

anoDeNascimento = int(input('Digite o seu ano de nascimento: '))

idade = datetime.datetime.now().year - anoDeNascimento

if idade > 18:
    print(f'Você passou já passou da idade de alistamento, você deveria ter se alistado a {idade - 18} anos atrás.')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para você chegar a idade de alistamento.')
else:
    print(f'Você deve se alistar esse ano!')

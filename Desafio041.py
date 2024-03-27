# Este programa lê o ano de nascimento de um atleta e mostra sua categoria
# de acordo com sua idade.
import datetime

anoDeNascimento = int(input('Digite seu ano de nascimento: '))

idade = datetime.datetime.now().year - anoDeNascimento

print(f'Você tem {idade} anos')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
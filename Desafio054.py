# Este programa lê o ano de nascimento de sete pessoas. No final, ele mostra
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

maiores = 0
menores = 0

for c in range(0, 7):
    ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = datetime.datetime.now().year - ano_de_nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Maiores de idade: {maiores}')
print(f'Menores de idade: {menores}')


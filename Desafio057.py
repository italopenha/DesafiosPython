# Este programa lê o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
# Caso receba outro valor, o programa pede uma nova digitação, até receber o valor correto.

sexo = ''

while sexo != 'm' and sexo != 'f':
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().lower()
    if sexo != 'm' and sexo != 'f':
        print('Valor deve ser M ou F!')

if sexo == 'm':
    print('Masculino!')
else:
    print('Feminino!')


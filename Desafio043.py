# Este programa lê o peso e a altura de uma pessoa e calcula seu IMC.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print(f'Você está abaixo do peso.')
elif imc <= 25:
    print(f'Você está no peso ideal.')
elif imc <= 30:
    print(f'Você está com sobrepeso.')
elif imc <= 40:
    print(f'Você está com obesidade.')
else:
    print(f'Você está com obesidade mórbida.')
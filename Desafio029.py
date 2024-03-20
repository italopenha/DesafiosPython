# Este programa lê a velocidade de um carro e mostra ao usuário se ele foi multado.

velocidade = int(input('Digite sua velocidade: '))

multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Sua velocidade foi de {velocidade} Km/h. Você foi multado em R$ {multa:.2f}.')
else:
    print(f'Sua velocidade foi de {velocidade} Km/h. Você não foi multado.')
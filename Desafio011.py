# Este programa lê a altura e a largura de uma parede e calcula a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

print(f'Para pintar uma parede de {area}m², será necessário {area / 2} litros de tinta.')
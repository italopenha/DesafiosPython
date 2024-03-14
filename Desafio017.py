# Este programa lê o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, e mostra o comprimento da hipotenusa.
import math

cOposto = float(input('Digite o cateto oposto: '))
cAdjacente = float(input('Digite o cateto adjacente: '))

# hipotenusa = math.sqrt(pow(cOposto, 2) + pow(cAdjacente, 2))
hipotenusa = math.hypot(cOposto, cAdjacente)

print(f'A hipotenusa é igual a {hipotenusa:.2f}')
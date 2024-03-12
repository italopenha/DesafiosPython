# Este programa lê um ângulo qualquer e mostra na tela o valor do
# seno, cosseno e tangente desse ângulo.
import math

angulo_em_graus = float(input('Digite um ângulo: '))

angulo_em_radianos = math.radians(angulo_em_graus)
seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

print(f'Seno: {seno:.4f}')
print(f'Cosseno {cosseno:.4f}')
print(f'Tangente: {tangente:.4f}')
# Este programa converte uma temperatura digitada em Celsius para Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = celsius * 1.8 + 32

print(f'{celsius:.0f}°C equivale a {fahrenheit:.2f}°F')
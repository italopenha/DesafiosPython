# Este programa lê o comprimento de três retas e diz se elas podem formar um triângulo.

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if abs(r2 - r3) < r1 and r1 < r2 + r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
elif abs(r1 - r3) < r2 and r2 < r1 + r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
elif abs(r1 - r2) < r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
else:
    print(f'As retas {r1}, {r2} e {r3} não formam um triângulo!')
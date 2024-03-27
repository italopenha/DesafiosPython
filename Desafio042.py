# Este programa lê o comprimento de três retas e diz se elas podem formar um triângulo
# e qual tipo de triângulo ele será.

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

eTriangulo = False

if abs(r2 - r3) < r1 and r1 < r2 + r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
    eTriangulo = True
elif abs(r1 - r3) < r2 and r2 < r1 + r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
    eTriangulo = True
elif abs(r1 - r2) < r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo!')
    eTriangulo = True
else:
    print(f'As retas {r1}, {r2} e {r3} não formam um triângulo!')

if eTriangulo:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Esse triângulo é equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é isósceles!')
    else:
        print('Esse triângulo é escaleno!')
"""Este programa tem uma função chamada area(), que recebe as dimensões de um terreno
retangular(largura e comprimento) e mostra a área do terreno."""

print(" Controle de Terrenos ")
print('-' * 20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))

def area(l, c):
    a = l * c
    print(f"A área de um terreno {l} x {c} é de {a}m².")

area(largura, comprimento)

"""Este programa simula o funcionamento de um caixa eletrônico. No início, ele
pergunta ao usuário qual será o valor a ser sacado(número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. Considerando que o
caixa possui cédulas de R$50, R$20, R$10 e R$1"""

valor = int(input('Qual valor você quer sacar? R$'))

cedulas = [50, 20, 10, 1]
continuar = True
contador = 0
resto = int

while continuar:
    if contador == 0:
        cedula = valor // cedulas[0]
        print(f'{cedula} nota(s) de R$ 50,00')
        resto = valor % cedulas[0]
    else:
        cedula = resto // cedulas[contador]
        resto = resto % cedulas[contador]

    if contador == 1:
        print(f'{cedula} nota(s) de R$ 20,00')
    elif contador == 2:
        print(f'{cedula} nota(s) de R$ 10,00')
    elif contador == 3:
        print(f'{cedula} nota(s) de R$ 1,00')

    contador += 1
    if resto == 0:
        continuar = False


'''cedula50 = valor // cedulas[0]
resto50 = valor % cedulas[0]
cedula20 = resto50 // cedulas[1]
resto20 = resto50 % cedulas[1]
cedula10 = resto20 // cedulas[2]
resto10 = resto20 % cedulas[2]
cedula1 = resto10 // cedulas[3]
resto1 = resto10 % cedulas[3]'''

'''print(f'{cedula50} nota(s) de R$ 50,00')
print(f'{cedula20} nota(s) de R$ 20,00')
print(f'{cedula10} nota(s) de R$ 10,00')
print(f'{cedula1} nota(s) de R$ 1,00')'''

# Este programa lê 4 nomes e sorteia um deles.
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

lista = [nome1, nome2, nome3, nome4]

nomeEscolhido = random.choice(lista)

print(nomeEscolhido)
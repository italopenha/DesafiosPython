"""Este programa tem uma lista chamada numeros e duas funções chamadas sorteia() e soma_par().
A primeira função sorteia 5 números e os coloca dentro da lista e a segunda função vai mostrar a
soma entre todos os valores PARES sorteados pela função anterior."""
from random import randint
from time import sleep

numeros = []

def sorteia(lista):
    print("Sorteando 5 valores da lista:", end=' ')
    for n in range(5):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.5)
    print("PRONTO!")

def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"Somando os valores pares de {lista}, temos {soma}.")

sorteia(numeros)
soma_par(numeros)

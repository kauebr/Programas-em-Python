#   Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
#   chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da
#   lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

numeros = []

def f0(lista):
    print('Sorteando 5 números entre 1 e 1000000:')
    for c in range(0, 5):
        lista.append(randint(1, 1000000))
        if c == 4:
            print(lista[c], end=";")
        else:
            sleep(0.3)
            print(lista[c], end="")
            sleep(0.2)
            print('...',end="")
    print()
def f1(lista):
    sleep(1)
    soma = 0
    qtd = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
            qtd += 1
    print(f'Foram digitados {qtd} valores pares e a soma entre eles resulta em {soma}')

f0(numeros)
print('-'*66)
f1(numeros)

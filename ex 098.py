# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    i = inicio
    f = fim
    p = passo
    f = 1
    while f == 1:
        if inicio < fim:
            while (inicio != fim):
                print(inicio, end=' ')
                inicio += passo
            print(fim)
            f = 0
        if inicio > fim:
            while(inicio != fim):
                print(inicio, end=" ")
                inicio = inicio + passo
            print)
        else:
            ()
contador(1, 10, 1)
contador(10, 0, -2)

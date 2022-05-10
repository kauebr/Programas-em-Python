'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
print('-'*33)
n = int(input('Escolha um número: '))
f = n
print('{}! = {} x '.format(n, n), end='')
while n != 0:
    if n == 2:
        print('{} = '.format(n - 1), end='')
        n = n -1
    elif n != 1:
        print('{} x '.format(n - 1), end='')
        n = n -1
    else:
        n = 0
        print(factorial(f))


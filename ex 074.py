'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
import random as rd
import math as mt
tu = (rd.randint(1, 100), rd.randint(1, 100), rd.randint(1, 100), rd.randint(1, 100), rd.randint(1, 100))
print('-'*33)
print('Tupla: ', tu)
print('Mínimo: ', min(tu))
print('Máximo: ', max(tu))
print('-'*33)
#  Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
#  O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
#  o programa se encerrará. Importante: use cores.
from random import randint
def ajuda(argumento):
    y = help(argumento)
    return y
def mudacor():
    print(f'\33[{randint(30, 37)};{randint(40, 47)};1m', end="")
def zeracor():
    print('\33[m \n')


# Programa Principal
while True:
    mudacor()
    x = input('Digite a função ou a biblioteca: ')
    if x == 'fim':
        break
    esse = ajuda(x)
    print(esse)
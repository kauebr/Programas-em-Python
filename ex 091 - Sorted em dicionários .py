# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
# tenham resultados aleatórios. Guarde esses resultados em um dicionário em
# Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.
print('-'*33)
from random import *
from time import *
from operator import *
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
c = 1
print('Valores Sorteados:')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar  {v[1]} no dado')
print('-'*33)


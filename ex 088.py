#  Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a
#  criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear
#  6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print(f'{"-"*40}')
numpal = int(input("Quantos números você deseja sortear?: "))
print(f'''{"-"*40}\n{'Palpites Mega Sena':.^40} ''')
print(f'{"-"*40}')
palpites = []
sublista = []
for palpitos in range(0, numpal):
    sublista = []

    c = 0
    while c != 7:
        x0 = randint(1, 100)
        if x0 not in sublista:
            sublista.append(x0)
            c += 1
    palpites.append(sublista)
c = 1
for l, palps in enumerate(palpites):
    print(f'Jogo {l}: {sorted(palps)}')
    sleep(1)






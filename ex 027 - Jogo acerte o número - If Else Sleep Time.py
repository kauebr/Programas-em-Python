# Crie um jogo em que o usuário pensa um número e o computador tenta acerta.

import random
import time
print('_-_'*11)
print('Vou pensar em um numero...')
time.sleep(2)
print('Estou pensando...')
time.sleep(4)
print('Já escolhi!')
ran = (random.randint(0, 3))
jog = int(input('tente advinhar o número que eu escolhi de 0 a 3: '))
print('Você escolheu ', jog)
print('Eu escolhi: ', ran)
print('Ganhou!' if jog == ran else 'Perdeu')
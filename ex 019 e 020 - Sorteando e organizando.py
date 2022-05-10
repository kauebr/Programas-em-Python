'''print('-'*33)
import random
a1 = input('Digite o nome do aluno [1]: ')
a2 = input('Digite o nome do aluno [2]: ')
a3 = input('Digite o nome do aluno [3]: ')
a4 = input('Digite o nome do aluno [4]: ')
sor = random.randint(1, 4)
def opcao1():
    print('Aluno sorteado: {}'.format(a1))
def opcao2():
    print('O aluno sorteado: {}'.format(a2))
def opcao3():
    print('O aluno Sorteado: {}'.format(a3))
def opcao4():
    print('O aluno sorteado: {}'.format(a4))
opcoes = {1:opcao1, 2:opcao2, 3:opcao3, 4:opcao4}

opcoes.get(random.randint(1,4))()'''
from random import shuffle
from random import choice
n1 = str(input('Digite o 1o aluno: '))
n2 = str(input('Digite o 2o aluno: '))
n3 = str(input('Digite o 3o aluno: '))
n4 = str(input('Digite o 4o aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))

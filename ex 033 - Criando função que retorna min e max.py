#  Crie um programa que lê 3 número e retorne o minimo e o max.

n1 = int(input('Digite o 1o. num: '))
n2 = int(input('Digite o 2o. num: '))
n3 = int(input('Digite o 3o. num: '))
min = n1
max = n1
if n2 < min:
    min < n2
if n3 < min:
    min = n3
if n2 > max:
    max = n2
if n3 > max:
    max = n3
print('Menor num: {}\nMaior num: {}'.format(min, max))
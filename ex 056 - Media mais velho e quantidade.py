'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
 mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
import os
mi = 0  # média idade;
hv = 0  # idade homem mais velho;
nhv = ''  # nome do homem mais velho;
mm = 0  # mulheres menores de idade;
for c in range(1, 5):
    n = input('Nome: ').strip()
    i = int(input('Idade: ').strip())
    s = input('Sexo [M/F]: ').lower().strip()
    mi += i
    if c == 1 and s == 'm':
        hv = i
        nhv = n
    else:
        hv = 0
    if s == 'm':
        if hv > i:
            hv = i
            nhv = n
    if s == 'f' and i < 20:
        mm += 1
mi = mi / 4
x = len(nhv)
print(
'''Homem mais velho: {}{}
Média de idade do grupo {}
Mulheres menores {}
'''.format(nhv[0].upper(), nhv[1:x], mi, mm))
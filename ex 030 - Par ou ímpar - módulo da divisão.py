#  Crie um programa que lê um número e retorna se é par ou impar.
n = int(input('Digite um numéro: '))
if n % 2 == 0:
    r = 'Par'
else:
    r = 'Ímpar'
print('{} é {}!'.format(n, r))


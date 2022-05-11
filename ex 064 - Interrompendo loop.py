'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag)'''
qtd = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número: '))
    qtd += 1
    soma += num
print('Foram digitados {} números e a soma entre eles equivale a: {}'.format(qtd, soma-999))

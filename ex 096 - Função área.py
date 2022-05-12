#  Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba
#  as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(b, a):
    print('-'*33)
    print(f"A àrea equivale à: {b * a}m²")


print('-'*33)
print('Controle de terrenos: ')
print('-'*33)
x = float(input('Digite a base em metros: '))
y = float(input('Digite a altura em metros: '))
area(x, y)

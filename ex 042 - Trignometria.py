#   Crie um programa que leia os três lados de um um poligno e retorne se ele é um triângulo equilátero, isósceles ou escaleno, ou se 
#   é um triângulo.


print('\33[96m='*33)
l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))
if l1<l2+l3 or l2<l1+l3 or l3<l1+l2:
    print('É um triângulo ', end='')
    if l1 == l2 and l3 == l1:
        print('equilátero!')
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print('isósceles!')
    else:
        print('escaleno!')
else:
    print('Não é um triângulo')


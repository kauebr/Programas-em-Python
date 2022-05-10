'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lis = [[], []]
for c in range(0,7):
    x = int(input(f'Digite o {c+1} valor: '))
    if x % 2 == 0:
        lis[0].append(x)
    else:
        lis[1].append(x)
print(f' Números pares: {sorted(lis[0])}')
print(f' Número ímpares: {sorted(lis[1])}')

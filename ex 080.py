'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
print('-'*33)
lis = []
for c in range(1, 4):
    print(lis)
    x0 = int(input(f'Digite o {c}º número: '))
    if c == 1:
        lis.append(x0)
        print('foi adicionado na posição 0')

    if c == 2:
        if x0 < lis[0]:
            lis.insert(0, x0)
        elif x0 == lis[0]:
            print('Número repetido, nada foi feito!')
        else:
            lis.insert(1, x0)
    if c ==3:
        if x0 in lis:
            print('Número repetido, nada foi feito!')
        elif x0 < lis[0]:
            lis.insert(0, x0)
        elif x0 < lis[1]:
            lis.insert(1, x0)
        else:
            lis.insert(3, x0)
            '''a partir daq !='''


print(lis)
'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
print('-'*33)
lis = []
for c in range(1, 11):
    print(lis)
    x0 = int(input(f'Digite o {c}º número: '))
    if c == 1:
        lis.append(x0)
        print('foi adicionado na posição 0')
    if c == 2:
        if x0 < lis[0]:
            lis.insert(0, x0)
            print('foi adicionado na posição 0')
        elif x0 == lis[0]:
            print('Número repetido, nada foi feito!')
        else:
            lis.insert(1, x0)
            print('foi adicionado na posição 1')
    if c ==3:
        if x0 in lis:
            print('Número repetido, nada foi feito!')
        elif x0 < lis[0]:
            lis.insert(0, x0)
            print('foi adicionado na posição 0')
        elif x0 < lis[1]:
            lis.insert(1, x0)
            print('foi adicionado na posição 1')
        else:
            lis.insert(2, x0)
            print('foi adicionado na posição 2')
    if c >= 4:
        for c in range(0, len(lis)):
            if x0 == lis[c]:
                print('Número repitido, nada foi feito!')
                break
            if x0 < lis[c]:
                 lis.insert(c, x0)
                 print('foi adicionado na posição ', c)
                 break
            elif x0 > lis[len(lis)-1]:
                lis.insert(len(lis)+1, x0)
                print(f'foi adicionado no final, posição {len(lis)-1}')
                break
print(lis)

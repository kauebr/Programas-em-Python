'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:'''

print('\33[91m-'*33)
print('{:-^33}'.format('LISTA DE COMPRAS'))
x = 's'
C = 1
flag0 = 's'
flag1 = total = caros = menor = nmenor= 0
while flag0 != 'n':
    print('\33[96m-'*33)
    prod = input(f'Insira o nome do produto {C}: ')
    prec = float(input(f'Digite o preço do produto {C} R$: '))
    total += prec
    if C == 1 or prec < menor:
        menor = prec
        nmenor = prod
    if prec > 1000:
        caros += 1
    while flag1 == 0:
        print('\33[91m-'*33)
        flag0 = input('Deseja continuar? [S/N]: ').strip().lower()[0]
        if flag0 in 'sn':
            flag1 = 1
            C += 1
        else:
            print('Ops, verifique!')
    flag1 = 0
print(f'''\33[96mTotal da compra: R${total:.2f}
QTD de produtos acima de R$1000,00: {caros}
Produto mais barato: {nmenor} (R$:{menor:.2f})''')

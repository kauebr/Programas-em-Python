'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
print('0'*33)
c = 1
f0 = 1
ls = []
lp = []
lo = []
while f0 == 1:
    x0 = int(input(f'Digite o {c}º número: '))
    ls.append(x0)
    if x0 % 2 == 0:
        lp.append(x0)
    else:
        lo.append(x0)
    while True:
        x1 = input('Deseja Continuar: [S/N]: ').lower().strip()
        if x1 not in 'sn':
            print('Não entendi :S')
        elif x1 == 'n':
            f0 = 0
            break
        else:
            break
    c += 1
print('0'*33)
print(f'''full list {ls}
Pair List {lp}
odd list {lo}
''')
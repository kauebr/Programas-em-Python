'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.'''
list = []
dado = []
c = 1
f0 = 1
mai = 0
print(f'.{"="*33}.')
while f0 == 1:
    dado.append(input((f'Digite o {c}º nome: ')))
    dado.append(int(input(f'Digite {c}º peso: ')))
    list.append(dado[:])
    if c == 1:
        min = dado[1]
    if dado[1] < min:
        min = dado[1]
    if dado[1] > mai:
        mai = dado[1]
    c += 1
    dado.clear()
    f1 = 1
    while True:
        x0 = input('Deseja continuar? [S/N]: ').lower().strip()
        if x0 == 's':
            break
        if x0 not in 'sn':
            print('ops não entendi!')
        if x0 == 'n':
            f0 = 0
            c -= 1
            break
pes = []
lev = []
for d in list:
    if d[1] == mai:
        pes.append(d[0])
    if d[1] == min:
        lev.append(d[0])
print(f'''Total de cadastrados = {c}
Mais pesados = {pes}
Mais leves = {lev}''')
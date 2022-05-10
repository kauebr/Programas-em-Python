import datetime
sn = 0 # SOMA DOS MENORES
si = 0 #SOMA DOS MAIORES
for c in range(1, 8):
    print('-'*33)
    x = int(input('Qual seu ano de nascimento?: '))
    f = (input('Já fez aniversário esse ano? [S/N]: '.lower()))
    y = datetime.date.today().year
    if f == 's':
        z = y-x
    else:
        z = y-x-1
    print('Sua idade é {}'.format(z))
    if z >= 18:
        si += 1
    else:
        sn += 1
    print('''MAIORES: {}
MENORES: {}'''.format(si, sn))
print('-'*33)
print('{:^33}'.format('RESULTADO'))
print('''MAIORES: {}
MENORES: {}'''.format(si, sn))
print('-'*33)
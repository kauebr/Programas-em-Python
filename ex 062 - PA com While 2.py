

pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Agora digite a razão: '))
c = 1
termo = pt
mais = 10
total = 0
while mais != 0:
    while c != mais+1:
        print('{} -> '.format(termo),end=' ')
        termo = termo + rz
        c += 1
        total += 1
    print('Pausa')
    mais = int(input('Deseja mostrar mais quanto termos?: '))
    c = 1
print('Progressão finaizada com {} termos'.format(total))

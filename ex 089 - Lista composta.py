# Exercício Python 089: Crie um programa que leia nome e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
print('_'*40)
c0 = 1
data = list()
temp = list()
f1 = 1
while f1 == 1:
    name = (input(f'Enter the {c0}st student name: '))
    n1 = float(input('Enter de 1st note: '))
    n2 = float(input('Enter de 2nd note:  '))
    avr = (n1 + n2)
    temp.append(name)
    temp.append(n1)
    temp.append(n2)
    data.append(temp[:])
    temp.clear()
    while True:
        f0 = input(('You want to continue [Y/N]: '.strip().lower()))
        if f0 not in 'yn':
            f0 = f0
            print('Try again')
        elif f0 == 'n':
            print('here')
            f1 = 0
            break
        elif f0 == 'y':
            c0 += 1
            print('-' * 40)
            break
print('-'*40)
print('No. NOME               Media')
for num, stu in enumerate(data):
        print(f'{num}  {stu[0]:<13}       {(stu[1]+stu[2])/2:}')
print('-'*40)
f2 = 1
while f2 == 1:
    f3 = int(input('Choose a student [999 to quit]:  '))
    if f3 == 999:
        break
    if f3 > len(data):
        print('Ops, try again...')
    else:
        print(f'{data[f3][0]} takes notes {data[f3][1]} and {data[f3][2]}')
        print('-'*40)
print('-'*40)
print('Come back alway! =)')

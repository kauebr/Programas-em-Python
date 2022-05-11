#  Faça uma taboada até cem


print('\33[95m{}{}'.format('-='*12, '-'))
num = int(input('Escolha um Número: '))
print('\33[95m{}{}'.format('-='*12, '-'))
print('Taboada do {}'.format(num))
for c in range(1, 101):
    print('{} x {:3} = {}'.format(num, c, num * c))

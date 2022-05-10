print('\33[95;4m-'*33)
num = int(input('\33[0;95mDigite um número: '))
p = int(input('Tipo de conversão\n[0] Para Binário\n[1] Para Octal\n[2] Para Hexadecimal\nESCOLHA: '))
if p == 0:
    num = bin(num)
    print('Binário: \33[32m{}\33[92;4m'.format(num[2::]))
elif p == 1:
    num = oct(num)
    print('Octal: {}'.format(num[2::]))
elif p == 2:
    num = hex(num)
    print('Hexadecimal: {}'.format(num[2::]))
else:
    print('\33[91mVocê digitou errado!, verifique por favor.')
print('\33[95;4m-'*33)
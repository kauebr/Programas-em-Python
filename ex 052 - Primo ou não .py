#   Crie um programa que leia um número inteiro e retorne se ele é primo ou não

num = int(input('Digite um número: '))
div = num
cp = 0
for c in range(1,  num+1):
    if num % c == 0:
        cp += 1
if cp == 2:
    print('\33[92m {} é um número primo, apenas divisivel por um e por ele mesmo.'.format(num))
else:
    print('\33[91m{} não é um número primo'.format(num))


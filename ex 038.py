print('\33[91m-'*33)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\33[92mO primeiro valor é maior!')
elif n2 > n1:
    print('\33[92mO segundo valor é maior!')
else:
    print('\33[92mNão existe maior, os dois são iguais!')
ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    i = int(input('Digite um número: '))
    if 0 <= i <= 20:
        break
    else:
        print('Ops, verifique e tente novamente')
print(ext[i])

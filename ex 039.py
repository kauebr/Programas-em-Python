print('\33[92m-'*33)
ida = int(input('Digite sua idade: '))
if ida == 18:
    print('Este é o ano para você se alistar!')
elif ida < 18:
    print('Ainda faltam {} para você se alistar'.format(18-ida))
else:
    print('Já se passaram {} anos do prazo de alistamento!'.format(ida-18))
print('\33[4m-'*33)


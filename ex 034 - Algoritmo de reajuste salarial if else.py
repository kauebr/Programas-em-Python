s = int(input('Digite seu salário R$: '))
if s >1200:
    a = 1.1
else:
    a = 1.15
print('Salário inicial R$ {:.2f}\nReajuste: {:.0f}%\nSálario atualizado R$ {:.2f}'.format(s, (a - 1)* 100, a*s))
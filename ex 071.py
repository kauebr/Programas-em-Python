valor = int(input('Informe o valor à ser sacado R$: '))
n50 = b20 = n10 = n1 = 0
if valor % 50 == 0:
   n50 = valor / 50
   valor  = 0
else:
    n50 = valor // 50
    valor = valor % 50
if valor % 20 == 0:
   n20 = valor / 20
   valor = 0
else:
    n20 = valor // 20
    valor = valor % 20
if valor % 10 == 0:
   n10 = valor / 10
   valor = 0
else:
    n10 = valor // 10
    valor = valor % 10
print(f'''Notas de 50 = {n50:.0f}
Notas de 20  = {n20:.0f} 
Notas de 10 = {n10:.0f}
Notas de 1 = {valor:.0f}''')
print('Acabei o mundo 2!!!')
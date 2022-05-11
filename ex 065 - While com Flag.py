#   Faça um loop while com flag

c = soma = 0
flag = flag1 =True
x = 's'
while flag:
    flag1 = True
    num = int(input('Digite o numero: '))
    if num == 33:
        break
    if x == 'n':
        flag = False
    else:
        if c == 0:
            min = num
            mai = num
        else:
            if num < min:
                min = num
            if num > mai:
                mai = num
    c += 1
    soma += num
    while flag1:
        x = input('Deseja continuar? ').lower().strip()
        if x == 's':
            flag1 = False
        elif x == 'n':
            flag1 = flag = False
        else:
            print('ops verifique...')
print('-'*33)
print('RESULTADO:')
print('''Media dos números digitados: {:.2f}
Menor número digitado {}
Maior número digitado {}'''.format(soma/c, min, mai))
print('-'*33)

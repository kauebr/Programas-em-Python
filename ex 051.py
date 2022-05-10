from time import sleep
print('-'*25)
print('\33[96m{:25}\33[m'.format('Progressão Aritimética'))
print('-'*25)
p = int(input('Digite o primeiro termo: '))
sleep(1)
print('Muito Bem!')
sleep(1)
r = int(input('Agora digite a razão: '))
sleep(1)
print('Vamos lá', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)
print('\33[96m{:25}\33[m'.format('Progressão:'))
num = p
for c in range(0, 10):
    print('{} '.format(num), end='→ ')
    num += r
print('ACABOU')

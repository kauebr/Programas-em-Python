from time import sleep
print ('\33[96mBy KC0D3\33[94mBR')
sleep(1)
for c in range (1, 15):
    print ('\33[96m-',end="")
    sleep(0.011235813)
    print('\33[m-',end="")
    sleep(0.011235813)
print('-')
print('{:^33}'.format('\33[96mDetector de Palindromos'))
for c in range (1, 14):
    print ('\33[96m-',end="")
    sleep(0.011235813)
    print('\33[m-',end="")
    sleep(0.011235813)
print ('\33[96m-',end="")
sleep(0.011235813)
print('\33[94m-',end='')
print('\33[m*')
sleep(0.011235813) # até aqui (pra cima) foi só codigo de cores;
z = input('\33[mDigite a frase: ') #salva o palindromo sem manipular a str pra usar no final;
x = z
x = x.replace(' ', '') #retira os espaços dentro da frase;
x = x.strip() # retira os espaços no inicio e no fim;
y = x[::-1] #cria uma variavel y de tráz pra frente
if y == x:
    print('\33[93m{} é um palindromo'.format(z))
else:
    print('\33[91m{} não é um palindromo!'.format(z))
print('\33[m{}{}'.format('-'*28, '*'))




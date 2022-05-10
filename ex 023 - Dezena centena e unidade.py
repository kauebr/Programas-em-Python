print('-'*55)
n = int(input('Digite um número inteiro de 1 a 9999: '))
u = n//1 %10
d = n//10 % 10
c = n//100 % 10
m = n//1000
print('Analisando o número {}'.format(n))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
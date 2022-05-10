#  Crie um programa que leia o nome completo de um usário e retorne seu primeiro e último nome.
print('.-.'*12)
n = str(input('Digite seu nome completo: ').strip())
n = n.split()
print('Muito prazer em te conhecer', n[0])
print('Primeiro nome: ', n[0])
print('Seu último nome é {}'.format(n[len(n)-1]))

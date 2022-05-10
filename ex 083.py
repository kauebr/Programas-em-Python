'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta'''
print(f'{".-"*16}.')
x0 = input('Digite sua expressão: ')
if (x0.count('(')) == (x0.count(')')):
    print('Parênteses corretos')
else:
    print('Parênteses incorretos')
print(f'{".-"*16}.')

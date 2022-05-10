'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
/A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
print('\33[96m-'*33)
t0 = int(input('Digite um número: '))
t1 = int(input('Digite um número: '))
t2 = int(input('Digite um número: '))
t3 = int(input('Digite um número: '))
tupla = (int(input('tupleie')), t1, t2, t3)
print('tupla: ', tupla)
print("Contagem de 9's: ", tupla.count(9))
print('Index do primeiro 3: ', tupla.index(3))
count = 0
for c in range(0, 4):
    if tupla[c] %2 == 0:
        count += 1
print('total de pares: ', count)


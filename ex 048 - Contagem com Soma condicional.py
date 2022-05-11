#   Faça um programa que conde de 3 ate 501 de 3 em 3 e no final mostre a soma dos valores multiplos de 3

s = 0
co = 0
for c in range(3, 501, 3):
    print(c)
    s += c
    co += 1
print('A soma dos {} valores multiplos de tres é igual a {}'.format(co, s))
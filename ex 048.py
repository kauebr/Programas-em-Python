s = 0
co = 0
for c in range(3, 501, 3):
    print(c)
    s += c
    co += 1
print('A soma dos {} valores multiplos de tres é igual a {}'.format(co, s))
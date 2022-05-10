s = 0
cp = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s += num
        cp += 1
print('A soma dos {} números pares digitados é {}'.format(cp, s))



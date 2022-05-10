print('\33[92m꧁\33[94;4mEspiral\33[m \33[94;4mFibona\33[96mcci\33[92;1mᨐᨐ\33[m\33[92m.: ')
loop = int(input('\33[94m Escolha o número de termos da sequência: '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
t3 = t1 + t2
print(t3, end=' ')
c = 3
while c != loop:
    t1 = t2
    t2 = t3
    t3 = t2 + t1
    print(t3, end=' ')
    c += 1

# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
ma = [[],[],[]]
for l in range(0, 3):
     for c in range(0, 3):
        if c == 0:
            coluna = 'A'
        if c == 1:
            coluna = 'B'
        if c == 2:
            coluna = 'C'
        ma[l].append(int(input(f'Digite {coluna}{l+1}: ')))
print(ma)
print()
s = 0
for c in range(0, 3):
    for l in range(0,3):
        print(ma[c][l], end =' ')
        s += ma[c][l]
    print()
print(f'-{"="*33}-')
print(f'Soma = {s}')
soma3 = 0
for l in range(0, 3):
    soma3 += ma[l][2]
print(f'Soma dos valores da 3a coluna = {soma3}')
print(f'Maximo da 2a linha = {max(ma[1])}')
print(f'-{"="*33}-')
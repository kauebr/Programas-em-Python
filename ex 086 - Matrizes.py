# Exercício Python 086: Crie um programa que declare uma matriz de
# dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela, com a formatação correta.
m = [[], [], []]
for l in range(0, 3): # 0
    for c in range(0, 3): # 00 01 02
        if c == 0:
            coluna = 'A'
        if c == 1:
            coluna = 'B'
        if c == 2:
            coluna = 'C'
        m[l].append(input(f'Digite {coluna}{l+1}: '))
print('      A       B       C')
for l in range(0,3 ):
    print(f'{l+1}  ',end="")
    for c in range(0, 3):
        print (f'[{m[l][c]:^5}]', end =' ')
    print()

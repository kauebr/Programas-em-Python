#   Crie uma formula para maior e menor com leitura de peso

i = 0
n = 0
for c in range(1, 5):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if c == 1:
        i = peso
        n = peso
    else:
        if peso > i:
            i = peso
        if peso < n:
            n = peso
print('''Maior peso: {} kg
Menor peso: {} kg'''.format(i, n))
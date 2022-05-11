'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
 termos da progressão usando a estrutura while.'''
print('Gerador de PA')
print('-'*22)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 10
total 0
while mais !=0:
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
print('Quanto termos quer mostrar mais: ')
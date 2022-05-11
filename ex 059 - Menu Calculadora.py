''''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
print('〷 ◠ ‿ ◠ 〷\n   Ex059\n')
caso = 0
while caso != 5:
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    caso = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\nEscolha: '''))
    if caso == 1:  #somar
        print('{:.0f} + {:.0f} = {:.0f}'.format(x, y, x + y))
    elif caso == 2:  #multiplicar
        print('{:.0f} x {:.0f} = {:.0f}'.format(x, y, x*y))
    elif caso == 3: # maior
        if x > y:
            print('O maior número entre {} e {} é {}'.format(x,y, x))
        else:
            print('O maior número entre {} e {} é {}'.format(x, y, x))
    elif caso == 5:  #encerrar while
        ()
    elif caso == 4:
        ()
    else:
        print('Ops, tente novamente')







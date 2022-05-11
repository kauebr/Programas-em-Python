#  Crie um prográma de crediário casas BAHIA!!

print('\33[96m-'*43)
val = float(input('Digite o valor do produto: '))
print('{:-^43}\n[1] À VISTA (dinheiro ou cheque) 10% off\n[2] À VISTA NO CARTÃO 5% off\n[3] ATE 2X NO CARTÃO sem desconto'.format(' Condição '))
print('[4] 3X OU MAIS NO CARTÃO 20% JURO')
r = int(input('ESCOLHA: '))
def opcao1():
    print('Valor final R$: {:.2f}'.format(val * 0.9))
def opcao2():
    print('Valor final R$: {:.2f}'.format(val * 0.95))
def opcao3():
    print('Valor final R$: {:.2f}'.format(val))
def opcao4():
    print('Valor final R$: {:.2f} '.format(val * 1.2))
opcoes = {1:opcao1, 2:opcao2, 3:opcao3, 4:opcao4}
opcoes.get(r)()
print('\33[96m-'*43)
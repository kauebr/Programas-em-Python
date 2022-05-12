'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
tupla = ('Arroz', 10, 'Oleo de soja', 20, 'Feijao', 8, 'Milho', 10, 'Azeite de oliva', 20, 'Coca cola 2l', 7,
         'Detergente', 2)
print('_'*33)
print('{:^33}'.format('LISTAGEM DE PREÇOS'))
print('_'*33)
for c in range (0, len(tupla)):
    if c % 2 == 0:
        print('{:.<15}.........R$: {:.2f}'.format(tupla[c], tupla[c+1]))
print('_'*33)

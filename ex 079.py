'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lis = []
print('\33[96m-'*50)
tl = int(input('Qual vai ser o tamanho da lista?: '))+1
for c in range(1, tl):
    x = int(input(f'Digite o {c}º valor a ser adcionado: '))
    if x in lis:
        print('já tem!, não foi adcionado')
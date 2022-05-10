#   Crie um programa que lê um ano e informa se ele é bissexto ou não

from datetime import date
ano = int(input('Digite o ano, coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
print('{} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else ('{} Não é bissexto'.format(ano)))
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))


#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS
# for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import time
from time import sleep
from datetime import date
print('-'*33)
mt = {'nome': input('Digite o nome: '),
      'nasc': int(input('Digite o ano de nascimento: ')),
      'ctps': int(input('CTPS (0) não tem: '))}
mt['idade'] = date.today().year - mt['nasc']
if mt['ctps'] != 0:
      mt['entrada'] = int(input('Digite o ano de entrada [aaaa]: '))
      mt['sal'] = int(input('Digite o  salário R$: '))
      mt['trabalhou'] = date.today().year - mt['entrada'] #contratacao
      mt['qposentara'] = (35- mt['trabalhou'] + mt['idade'])
f0 = 0
print('-'*33)
if mt['ctps'] != 0:
      for c, v in mt.items():
            time.sleep(1)
            if f0 == 3:
                  break
            print(f'- {c} tem valor {v} ')
            f0 += 1
      print('-'*33)
f0 = 0
if mt['ctps'] == 0:
      for c, v in mt.items():
            print(f'- {c} tem valor {v}')
      quit()

for v in mt.values():
      if f0 == 0:
            print(f'{v} tem ',end='')
      if f0 == 3:
            print(v, 'anos de idade, ', end="")
            ida = v
      if f0 == 6:
            print(f'trabalhou durante {v} anos e ',end="")
      if f0 ==7:
            print(f'vai se aposentar com {v} anos.')
      f0 +=1


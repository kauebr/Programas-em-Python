
#   Crie um programa que lei o valor de uma casa o sálario e em quantos anos ele deseja pagar, sendo que a parcela tem que ser inferior
#   à 30% do salário do contratante, caso contrato retorne mensagem de erro.

#By: KCODEBR


from time import sleep
print('\33[96m-'*33, '\33[93m')
val = int(input('Digite o valor da casa R$: '))
sal = int(input('Digite seu sálario R$: '))
per = int(input('Em quantos anos deseja pagar: '))
sleep(1)
print('\33[97m ...CALCULANDO', end="")
sleep(1.5)
print('.', end="")
sleep(.7)
print('.', end="")
sleep(.7)
print('.')
sleep(.7)
print('\33[96m-'*33)
sleep(1)
print('\33[97mRESULTADO :')
sleep(1)
mes = per * 12
parc = val / mes
if parc > sal * 0.3:
    print('Valor da parcela R$: {:.2f}'.format(val/mes))
    print('\33[91mERRO: EXECEDE O VALOR MAXIMO PERMITIDO POR PARCELA')
else:
    print('\33[92mAprovado!')
    print('\33[96mSerão {} parcelas de R$: {:.2f}'.format(mes, val/mes))
print('\33[96m-' * 33, '\33[93m')


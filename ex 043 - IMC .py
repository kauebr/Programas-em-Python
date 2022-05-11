#  Crie um programa que cálcule o IMC de um usuário

from time import sleep
print('\33[92m-'*33)
print('\33[91m{:=^33}'.format('CÁLCULO IMC'))
print('\33[92m-'*33)
peso = float(input('\33[91mDigite seu peso: '))
sleep(0.3)
print('Muito bem!')
sleep(0.3)
a = float(input('Agora digite sua altura: '))
print('\33[92m-'*33)
print('\33[91m{:=^33}'.format('R E S U L T A D O'))
print('\33[92m-'*33)
imc = peso/(pow(a, 2))
print('Seu IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30<= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
print('\33[92m-'*33)




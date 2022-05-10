#   Crie um programa que informa se o usuário foi multado ou não, para multas considere acima de 80 km
V = float(input('Qual a velocidade atual do carro? em KM: '))
if V > 80:
    print('Você foi multado!\nUltrapassou a veloidade em {:.1f} KM\nValor da multa: R$ {:.2f}'.format(V-80, (V-80)*7))
else:
    print('Não foi multado!')




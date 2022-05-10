from math import radians, cos, sin, tan, degrees
print("-"*33)
ang = float(input('Digite o ângulo: '))
ang = radians(ang)
cos = cos(ang)
sen = sin(ang)
tang = tan(ang)
print('ÂNGULO: {:.0f};\nSENO: {:.2f};\nCOSSENO: {:.2f};\nTANGENTE: {:.2f};'.format(degrees(ang), sen, cos, tang))
print('-'*33)

#   Crie um programa que eia uma distânca e cálcule o custo, se for menor igual a 200 km são 50 centavos por km, se for mais que 200 km serão 45 centavos por km

print('---'*15)
dist = float(input('Informe a distância de sua viagem em kms: '))
print('---'*15)
pre = dist * 0.50 if dist < 201 else dist * 0.45
print('DISTANCIA: {}\n\nTOTAL R$: {:.2f}'.format(dist, pre))

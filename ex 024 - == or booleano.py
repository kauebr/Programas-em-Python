#  Crie um programa que identifique se uma pessoa nasceu em uma cidade que começa com santa
nome = input('Em qual cidade voce nasceu?: ')
nome = nome.split()
print(nome[0].lower() == ('santo') or nome[0].lower() == ('santa') )
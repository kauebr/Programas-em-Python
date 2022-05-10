# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
temp = dict()
mulheres = []
dados = []
f0 = 1
galera = totida = 0
idades = []
while f0 == 1:
    temp['Nome'] = input('Digite o nome: ')
    galera += 1
    while True:
        temp['Sexo'] = input('Informe o sexo [M/F]: ').strip().lower()
        if temp['Sexo'] in 'mf':
            if temp['Sexo'] == 'f':
                mulheres.append(temp['Nome'])
            break
        else:
            print('Ops, verifique!')
    temp['Idade'] = int(input('Informe a idade: '))
    totida += temp['Idade']
    idades.append(temp['Idade'])
    dados.append(temp)
    temp.clear
    while True:
        x = input('Deseja continuar? [S/N]: ').strip().lower()
        if x not in 'sn':
            print('Digite apenas S ou N')
        if x == 's':
            break
        if x == 'n':
            f0 = 0
            break
print('-'*33)
print(f'Galera: {galera}')
print(f'Média de idade: {totida/galera:.2f}')
print('Lista de mulheres:', mulheres)
print('Idades acima da média: ', end="")
for v in idades:
    if v > (totida/galera):
        print(v,end=" ")
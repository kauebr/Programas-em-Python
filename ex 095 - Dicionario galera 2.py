# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''Cada jogado é um dicionário'''
todos = list()
dic = dict()
f0 = 's'
gols = []
c = 1
while f0 == 's':
    print('-'*66)
    dic['nome'] = input(f'Digite o nome {c}º do jogador: ')
    partidas = int(input('Número de partidas: '))
    c += 1

    dic['gols'] = list()
    dic['total'] = list()
    xtotal = 0
    for c in range(0, partidas):
        dic['gols'].append(int(input(f'Quantos Gols na partida {c+1}: ')))
        xtotal += dic['gols'][c] # aqui tinha erro tem que por o lugar da lista nao pode somar a lista toda
    print('-'*66)
    dic['total'] = xtotal
    todos.append(dic.copy())
    dic.clear()
    while True:
        f0 = (input('Deseja Continuar [S/N]?: ').lower().strip())
        if f0 in 'sn':
            break
        else:
            print('Digite apenas S ou N')
        if f0 == 'n':
            break
print('-'*66)
# nome da lista geral é todos, dentro da lista tem dicionarios  com os valores abaixo:
print('Cód  Nome           Gols                             Total     ')
for c in range(0, len(todos)):
    print(f"{c+1:<5}{todos[c]['nome']:<15}{str(todos[c]['gols']):<33}{todos[c]['total']}")
print('-'*66)
f0 = 0
while f0 != 999:
    f0 = int(input('Digite o Jogador que deseja saber: '))
    print(f0)
    f0 = f0 -1
    print(f0)
    print(f" O jogador {todos[c]['nome']} fez: ")
    if f0 == 999:
        print('<<<VOLTE SEMPRE>>>')
        quit()
    for c in range(0, len(todos[f0]["gols"])):
        print(f"{todos[f0]['gols'][c]} gols na {c+1} partida;")
    print('-'*66)



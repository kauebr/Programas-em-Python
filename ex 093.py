#   Exercício Python 093: Crie um programa que gerencie o aproveitamento de um
#   jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
#   ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
#   tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o
#   campeonato.
dic = dict()
print('-'*33)
dic['Nome'] = input('Digite o nome do jogador: ')
partidas = int(input('Número de partidas: '))
gols = []
total = 0
for c in range(0, partidas):
    x = int(input(f'Quantos Gols na partida {c+1}: '))
    gols.append(x)
    total += x
dic['gols'] = gols
dic['total'] = total
print('-'*33)
print(f'{dic}, Total de gols {total}')
print('-'*33)
for c, v in(dic.items()):
    print(f'- o campo {c} tem valor {v}')
print('-'*33)
print(f'O jogador {dic["Nome"]}  jogou {len(dic["gols"])} partidas')
for c,v in enumerate(gols):
    print(f'=> Na partida {c+1}, fez {v} gols.')
print('-'*33)

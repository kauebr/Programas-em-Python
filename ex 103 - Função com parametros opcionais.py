#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
# de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador, gols):
    if j == '':
        jogador = '<desconhecido>'
    if g == '' or g.isalpha():
        gols = 0
    print(f"O jogador {jogador} fez  {gols} Gols!")


j = input('Digite o nome do jogador: ')
g = input('Digite o núero de gol(s): ')
ficha(j, g)
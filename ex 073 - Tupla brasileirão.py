'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
tabela = ('America - MG', 'Athletico Paranaense - PR', 'Atlético - GO', 'Atletico Mineiro - MG', 'Avaí - SC', 'Botafogo - RJ', \
         'Ceará - CE', 'Corinthians - SP', 'Coritiba - PR', 'Cuiabá - MT', 'Flamengo - RJ', 'Fluminense - RJ', \
         'Fortaleza - CE', 'Goiás - GO', 'Internacional - RS', 'Juventude - RS', 'Palmeiras - SP', \
         'Red Bull Bragantino - SP', 'Santos - SP', 'São Paulo - SP')
print('-'*33)
print('TOP 5:')
for c in range(0, 5):
    print(f'{c+1}º Colocado: {tabela[c]}')
print('-'*33)
print('Últimos 4:')
for c in range(16, 20):
    print(f'{c+1}º colocado: {tabela[c]}')
print('-'*33)
print('Ordem Alfabetica:')
print(sorted(tabela))
print('-'*33)
print(f'O Furacão esta na {1+tabela.index("Athletico Paranaense - PR")}ª posição')



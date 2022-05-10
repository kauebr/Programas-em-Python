# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.

print('-'*33)
aluno = dict()
aluno['nome'] = input('Digite o nome: ')
aluno['nota'] = int(input(f'Digite a nota de {aluno["nome"]}: '))
if aluno['nota'] > 7:
    aluno['situação'] = ('Aprovado')
elif aluno['nota'] < 4:
    aluno['situação'] = ('reprovado')
else:
    aluno['situação'] = ('em recuperação')
print(f'O aluno {aluno["nome"]} tirou nota {aluno["nota"]} e esta {aluno["situação"]}')
for k, v in aluno.items():
    print(f'- {k} é {v}')
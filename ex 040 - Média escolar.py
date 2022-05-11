#  Crie um programa que leia duas notas de um aluno x e retorne se ele esta em recuperacao, reprovado ou aprovado, considere média sete, e abaixo de 5 reprovado! 

print('\33[94m-'*35)
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
med = (n1 + n2)/2
if med < 5:
    print('\33[91mAluno reprovado!')
elif med >= 5 and med < 7:
    print('\33[93mAluno em recuperação!')
else:
    print('\33[92mAluno aprovado!')
print('\33[94m-'*33)
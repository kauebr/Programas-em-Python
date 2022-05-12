''''Exercício Python 081: Crie um programa que vai ler vários números e colocar
 em uma lista.
 Depois disso, mostre:
 A) Quantos números foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.'''
print('-'*33)
c = 1
lis = [1, 2, 3]
print(lis.sort(reverse=True))
while True:
    x0 = int(input(f'Digite o {c}º número: '))
    lis.append(x0)
    c += 1
    x1 = input('Deseja continuar [S/N]: ').lower().strip()
    if 'n' in x1:
        break

print(f'Total de números digitados: {c-1}')
if len(lis) > 1:
    lis.sort(reverse=True)
    print(f'lista inversa: {lis}')
else:
    print(f'lista: {lis}')
if 5 in lis:
    print('Valor 5 esta foi digitado')
else:
    print('Valor 5 não foi digitado')

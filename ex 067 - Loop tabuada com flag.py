#  Faça um leitor que pergunte um número e mostre a tabuada dele, e só sera interrompido quando o usuário digitar 0

print('-'*33)
num = 0
c = 1
while True:
    num = int(input('Escolha o número da táboada: '))
    if num <0:
        break
    for c in range(1,11):
        print(f'''{num} x {c:3} = {num*c}''')
    print('-' * 33)

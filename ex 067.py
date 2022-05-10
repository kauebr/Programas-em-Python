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

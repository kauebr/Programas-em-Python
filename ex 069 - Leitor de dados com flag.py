#   Faça um programa que leia a idade e o sexo e pergunte se o usuário deseja continuar, no final mostre todos os maiores de Idade
#   E depois mostre a some dos maiores de idade, dos homens e das mulheres com menos de 20 anos

sm = sh = sf = brk = 0
while True:
    if brk == 1:
        break
    id = int(input('Digite a idade: '))
    if id > 18:
        sm += 1
    sex = 'x'
    while sex not in 'MmFf':
        sex = (input('Digite o Sexo [M/F]: ')).strip().lower()[0]
        if sex not in 'mf':
            print('Ops, verifique!')
        elif sex == 'm':
            sh += 1
        else:
            if id < 20:
                sf +=1
        x = 'x'
        while x not in 'sn':
            x = input('Deseja continuar? [S/N]: ').strip().lower()[0]
            if x not in 'sn':
                print('Ops, verifique!')
            if x == 'n':
                brk = 1
print(33*'-')
print(f'Maiores: {sm}\nHomens: {sh}\nMulheres com menos de 20 anos: {sf} ')

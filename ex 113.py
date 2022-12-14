'''def leiaInt(numero):
    valor = x
    while True:
        if x.isalpha() or valor.isalpha():
            print('erro')
            valor = input('Digite o valor: ')
        if x.isnumeric() or valor.isnumeric():
            valor = in t(valor)
            print('Voce digitou', valor)
            break


x = input('Digite um valor: ')
leiaInt(x)
print('E mais uma vez repito, você digitou:', x)'''
flag = 0
while flag != 1:
    try:
        x = int(input('Digite um número inteiro: '))
        flag = 1
    except as erro:
        print(f'Ops, tivemos um erro: {erro}')




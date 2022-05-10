# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(numero):
    valor = x
    while True:
        if x.isalpha() or valor.isalpha():
            print('erro')
            valor = input('Digite o valor: ')
        if x.isnumeric() or valor.isnumeric():
            valor = int(valor)
            print('Voce digitou', valor)
            break


x = input('Digite um valor: ')
leiaInt(x)
print('E mais uma vez repito, você digitou:', x)

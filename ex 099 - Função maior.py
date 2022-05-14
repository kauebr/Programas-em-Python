# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* lis):
    c = 1
    tot = 0
    if lis == ():
        m = 'nenhum'
    for num in lis:
        tot += 1
        if c == 1:
            m = num
        elif num > m:
            m = num
    print('-'*33)
    print(f"Valores informados = {tot} \nO maior é = {m}")
    print('-'*33)


maior(1,2,3,4,10,33)
maior(1)
maior()





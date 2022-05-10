#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime
hj = (datetime.date.today().year)


def voto(ano_nasc):
    x = hj - ano_nasc
    if x < 18:
        return ('NEGADO')
    elif x <65:
        return('OBRIGATÓRIO')
    else:
        return('OPCIONAL')


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
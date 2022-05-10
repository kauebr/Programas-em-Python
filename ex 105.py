# Exercício Python 105: Faç
# vai retornar um dicionári
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*num, sit=False):
    '''

    :param num: coloque as notas
    :param sit: padrao falso, mostra a situacao
    :return: retorno variavel
    '''

    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num)/len(num)
    if sit:
        if r['Média'] <=  4:
            r['Situação'] = 'Péssima'
        elif r['Média']  <= 7:
            r['Situação'] = 'Paia em'
        else:
            r['Situação'] = 'topz'
    return r


resposta = notas(0, 9.4, 3, 7, 10, sit=True)
print(resposta)
help(notas)







# programa principal

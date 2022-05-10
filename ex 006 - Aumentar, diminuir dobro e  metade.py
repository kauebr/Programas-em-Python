#  Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
#  diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(num, fromat=True):
    num *= 1.1
    return num if fromat is False else (f"R${num:.2f}")
def diminuir(num, fromat=True):
    num *= 0.9
    return num if fromat is False else (f"R${num:.2f}")
def dobro(num, fromat=True):
    num *= 2
    return num if fromat is False else (f"R${num:.2f}")
def metade(num, fromat=True):
    num *= 0.5
    return num if fromat is False else (f"R${num:.2f}")
def resumo(num):
    print(33*'-')
    print(f'{"Resumo do Valor":^33}')
    print(33*'-')
    print(f'{"Valor Analisado":24}{"R$"}{num:.2f}')
    print(f'''{"Aumentado fica":24}{aumentar(num)}
{"Diminuido fica":24}{diminuir(num)}
{"O dobro vale":24}{dobro(num)}
{"A metade é":24}{metade(num)}''')
    print(33*'-')
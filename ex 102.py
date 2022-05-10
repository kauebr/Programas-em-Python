# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou  não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """

    :param numero: digite o número
    :param show: padrao False, digite True se quiser mostrar o descritivo
    """
    f = numero
    for c in range(numero-1, 0, -1):
        f *= c
    print(f"O fatorial de  {numero} é {f}")
    if show:
        print(f"{numero} x",end=" ")
        for c in range(numero - 1, 1, -1):
            print(f'{c} x',end=" ")
        print(f"1 = {f}")

#progama principal


fatorial(5, show=True)


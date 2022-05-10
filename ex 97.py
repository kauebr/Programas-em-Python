# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def borda(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(texto)
    print('-' * tam)
borda('Kaue')
borda('vai aprende')
borda('programee')



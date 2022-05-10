'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
print('-'*39)
nums = []
for c in range(0, 5):
    nums.append(int(input('Digite um numero para adcionar!: ')))

print('lista: ', nums)
print('menor valor da lista: ', min(nums), 'na posição: ', nums.index(min(nums))+1)
print('maior valor da lista: ', max(nums), 'na posição: ', nums.index(max(nums))+1)

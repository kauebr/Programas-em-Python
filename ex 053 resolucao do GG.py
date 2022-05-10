'''frase = input('Digite uma frase: ').strip()
print(frase)
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(inverso)'''

x = input('Digite uma frase: ').strip().split()
y = ''.join(x)
z = ""
print(y)
for c in range(len(y)-1, -1, -1):
    z = z + y[c]
print(z)



#   Faça um loop while sendo parado com break

print('-'*25)
s = c = 0
while True:
    n = int(input('Digite um número :'))
    if n == 999:
        break
    s += n
    c += 1
    print('-' * 25)
print(f'Finalizado!\nForam digitados {c} números;\nA soma ficou em {s}')

wds = ('pao', 'feijao', 'macarrao', 'batatinha', 'cenoura', 'cabotia', 'zuchinni')
print('-'*36)
for c in range(0, len(wds)):
    var = wds[c]
    print(f'Na palavra {var} temos: ', end='')
    for c in range(1, len(var)):
        if var[c] in 'aeiou':
            print(var[c], end=' ')
    print()
print('-'*36)

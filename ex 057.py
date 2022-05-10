n = input('Digite o sexo [M/F]: ').strip().upper()[0]
while n not in ('F', 'M'):
    print('Ops. Algo errado!')
    n = input('Digite o sexo [M/F]').strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(n))
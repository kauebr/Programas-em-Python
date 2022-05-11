#   Faça um programa de registro de sexo com a função while tratando str e mandando mensage de erro em registro incorreto.

n = input('Digite o sexo [M/F]: ').strip().upper()[0]
while n not in ('F', 'M'):
    print('Ops. Algo errado!')
    n = input('Digite o sexo [M/F]').strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(n))
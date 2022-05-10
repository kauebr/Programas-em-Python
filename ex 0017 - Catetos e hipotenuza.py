import math
print('='*20)
opo = int(input('Digite o cateto oposto: '))
adj = int(input('Digite o cateto adjacente: '))
hip = math.hypot(opo, adj)
print('A soma dos quadrados de {} e {} é igual á {:.0f}'.format(opo, adj, hip))

meta = 10000
from math import trunc
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

vendedores = []
melhor_vendedor = []
for i, vendedor in enumerate(vendas):
    if vendas[i][1] >= meta:
        vendedores.append(vendas[i])
    melhor_vendedor = (max(vendedores))
porcentagem = (len(vendedores) * 100) / len(vendas)
print('{}% dos vendedores atingiram a meta de vendas.'.format(porcentagem.__trunc__()))
print('O(A) melhor vendedor(a) foi {} com um total de {} vendas.'.format(melhor_vendedor[0], melhor_vendedor[1]))

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
for i, vendedor in enumerate(vendas):
    if vendas[i][1] >= meta:
        vendedores.append(vendas[i])
porcentagem = (len(vendedores) * 100) / len(vendas)
print('{}% dos vendedores atingiram a meta de vendas.'.format(porcentagem.__trunc__()))

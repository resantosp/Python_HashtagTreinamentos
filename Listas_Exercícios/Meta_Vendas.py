meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
for vendedor in vendas:
    indice = vendas.index(vendedor)
    if vendas[indice][1] < meta:
        print('{} não bateu a meta mensal. Total de vendas: {}'.format(vendas[indice][0], vendas[indice][1]))

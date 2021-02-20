meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
for i, vendedor in enumerate(vendas):
    if vendas[i][1] < meta:
        print('{} não bateu a meta mensal. Total de vendas: {}'.format(vendas[i][0], vendas[i][1]))

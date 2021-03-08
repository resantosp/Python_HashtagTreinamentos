venda = input('Registre um produto (para finalizar o registro de novos produtos, basta dar enter com a caixa vazia): ')
vendas = []
while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto (para finalizar o registro de novos produtos, basta dar enter com a caixa vazia): ')
print('Registro finalizado. Os produtos registrados foram: {}.'.format(vendas))

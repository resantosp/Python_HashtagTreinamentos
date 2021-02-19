'''
Digamos que você trabalhe em uma empresa de ecommerce

1. Calcular 10% de imposto sobre o valor dos livros
2. Alterar o registro dos preços dos livros da empresa
3. Ajustar o novo valor na tabela
4. Calcular quanto que o imposto vai aumentar de custo para a empresa??

Obs: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
'''

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']
#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i = produtos.index('livro')
    total1 = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    novo_valor = int(produtos_ecommerce[i][1] + ((10 / 100) * produtos_ecommerce[i][1]))
    produtos_ecommerce[i][1] = novo_valor
    total2 = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    custo = total2 - total1
    print('O novo valor do produto será R${}.'.format(novo_valor))
    print('O impacto financeiro do aumento de 10% no imposto será de R${:.2f}.'.format(custo))
else:
    print('Não haverá impactos no setor financeiro decorrente da mudança da carga tributária sobre livros.')    
    
'''
OBJETIVOS:
1 - Apresentar o melhor e o pior mês
2 - Apresentar o número total de vendas
3 - Apresentar quanto do valor total de vendas o melhor mês representa (%)
4 - Apresentar um TOP 3 dos maiores valores de venda
'''
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [852, 8456, 4512, 8465, 6531, 8451]
vendas_2sem = [8465, 9645, 7454, 9743, 8512, 6354]
vendas = vendas_1sem + vendas_2sem
print('='*10, 'RELATÓRIO DE VENDAS 2020', '='*10, '\n')
melhor = max(vendas)
indice_melhor = vendas.index(melhor)
print('O melhor mês do ano foi {} com {} vendas.'.format(meses[indice_melhor].upper(), melhor))
pior = min(vendas)
indice_pior = vendas.index(pior)
print('O pior mês do ano foi {} com {} vendas.'.format(meses[indice_pior].upper(), pior))
print('O número total de vendas em 2020 foi:    {}.'.format(sum(vendas)))
porcentagem = melhor * 100 / sum(vendas)
print('O mês de {} representou {:.2f} por cento (%) do faturamento total anual.'.format(meses[indice_melhor].upper(), porcentagem))
top3 = [melhor]
for lista in range(1, 3):
    vendas.remove(max(vendas))
    top3.append(max(vendas))
print('Os valores referentes aos três melhores meses do ano foram: \n1. {} \n2. {} \n3. {}'.format(top3[0], top3[1], top3[2]))
#top1 = max(vendas)
#vendas.remove(max(vendas))
#top2 = max(vendas)
#vendas.remove(max(vendas))
#top3 = max(vendas)
#print('Os valores referentes aos três melhores meses do ano foram: \n1. {} \n2. {} \n3. {}'.format(top1, top2, top3))

print('='*10, 'RESORT PARADISE', '='*10)
print(' '*7, 'Seu paraíso na Terra...', ' '*7)
print('='*8, 'SISTEMA DE CADASTRO', '='*8)
print('\n')

qtd_hospedes = int(input('Quantidade de hóspedes: '))
quarto = []
for hospedes in range(qtd_hospedes):
    print('     HÓSPEDE {}'.format(hospedes + 1))
    nome = input('NOME: ')
    cpf = input('CPF: ')
    hospede = [nome, cpf]
    quarto.append(hospede)
print('\n', '='*8, 'DADOS DO QUARTO', '='*8)
for i in quarto:
    indice = quarto.index(i)
    print('NOME: {}   '.format(quarto[indice][0]),'CPF: {}'.format(quarto[indice][1]))


##problemas extras:
#1. tentar colocar uma pessoa a menos
#2. digitar cpf errado/inválido
n = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = n // 86400
n = n % 86400
horas = n // 3600
print(dias, 'e', horas)

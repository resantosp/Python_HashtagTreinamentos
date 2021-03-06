n = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = n // 86400
n = n % 86400
horas = n // 3600
n = n % 3600
minutos = n // 60
segundos = n % 60
print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')

# Entrada
print('Um programa que receba segundos e transforme em horas, minutos e segundos:')
segundo_1 = float(input('Digite aqui o número de segundos: '))

# Meio do problema
hora = segundo_1 // 3600
resto = segundo_1 % 3600
minuto = resto // 60
segundo_2 = resto % 60

# Final
print('Por isso, representa-se por: ', hora, 'horas,', minuto, 'minuto(s) e', segundo_2, 'segundos')

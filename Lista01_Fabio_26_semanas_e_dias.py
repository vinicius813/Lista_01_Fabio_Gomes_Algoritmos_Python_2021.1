# Entrada
print('Escreva um programa que transforma dias em semanas e dias:')
dia = float(input('Digite aqui o número de dias: '))

# Conversão
semana = dia / 7
dias_total = dia % 7

# Final
print('A conversão de dia em semanas e dias será: ', semana, 'semanas e', dias_total, 'dias')
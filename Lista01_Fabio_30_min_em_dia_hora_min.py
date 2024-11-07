# Entrada
print('Um programa que receba minutos e transforme em dias, horas e minutos:')
minutos = float(input('Digite aqui o número de minutos: '))

# Processamento
min_dias = minutos // 1440
resto = minutos % 1440
min_horas = resto // 60
min_totais = resto % 60

# Fim
print('A conversão de minutos em dias, horas e minutos será: ', min_dias, 'dias,', min_horas, 'horas e', min_totais, 'minutos')
# Entrada
print('Um programa que leia um número inteiro de metros e converta para quilômetro e metro:')
metro = float(input('Digite aqui o número de metros: '))

# Meio
km = metro / 1000
metro_totais = metro % 1000

# Fim
print('A quantidade calculada para quilômetro e metro será: ', km, 'quilômetros e', metro_totais, 'metros')

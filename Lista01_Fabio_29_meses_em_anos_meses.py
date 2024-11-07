# Introdução
print('Um programa que receba meses e transforme em anos e meses:')
meses = float(input('Digite quantos meses: '))

# Metade
anos = meses // 12
meses_total = meses % 12

# Final
print('A conversão de meses em anos e meses será: ', anos, 'anos e', meses_total, 'meses')

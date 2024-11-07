# Entrada
print('Um programa que leia uma idade em dias e expresse em anos, meses e dias:')
dia = float(input('Digite a idade de uma pessoa em dias: '))

# Processamento
dias_ano = dia // 365
resto_1 = dia % 365
dias_meses = resto_1 // 12
dias_2 = resto_1 % 12

# O somatório total
sub_total = dias_ano + dias_meses + dias_2

# Saída
print('A solução de dias para anos, meses e dias é: ', dias_ano, 'anos,', dias_meses, 'meses e', dias_2, 'dias')

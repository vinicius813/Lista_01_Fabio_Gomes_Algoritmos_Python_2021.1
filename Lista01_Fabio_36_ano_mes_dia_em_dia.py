# Introdução
print('Transforme a idade de uma pessoa de anos, meses e dias em apenas dias:')
anos = int(input('Escreva o número de anos: '))
meses = int(input('Escreva o número de meses: '))
dias = int(input('Escreva o número de dias: '))

# Meio da questão
anos_dias = anos * 365
meses_dias = meses * 30

# Somatório de dias
sub_total = anos_dias + meses_dias + dias

# Impressão
print('O valor total em dias é: ', sub_total, 'dias')
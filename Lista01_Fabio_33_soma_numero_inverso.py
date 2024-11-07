# Entrada
print('Questão sobre a soma de um número inteiro de 3 dígitos com seu inverso:')
num_1 = float(input('Digite aqui o número: '))

# Processamento
unidade = num_1 // 100
resto_1 = num_1 % 100
dezena = resto_1 // 10
centena = resto_1 % 10
num_2 = centena * 100 + dezena * 10 + unidade * 1

# Calcular o somatório de seu inverso
sub_total =  num_1 + num_2

# Saída
print('A soma de um número com seu inverso será: ', sub_total)


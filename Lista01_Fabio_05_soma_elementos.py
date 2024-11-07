# Leitura de número
print('Diga aqui a soma de um número com 3 dígitos: ')
num_1 = int(input('Escreva um número de 3 dígitos: '))

# Meio da questão
centena = num_1 // 100
resto_1 = num_1 % 100
dezena = resto_1 // 10
unidade = resto_1 % 10
resto_totais = centena + dezena + unidade

# Soma dos elementos
print('A soma de seus elementos é: ', resto_totais)
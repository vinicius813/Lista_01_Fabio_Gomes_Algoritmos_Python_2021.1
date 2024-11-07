# Introdução
print('Leia um número de 3 dígitos e calcule a diferença o número e seu inverso:')
num_1 = float(input('Digite aqui o número: '))

# Meio do problema
unidade = num_1 // 100
resto_1 = num_1 % 100
dezena = resto_1 // 10
centena = resto_1 % 10
num_2 = centena * 100 + dezena * 10 + unidade * 1

# Calcular a diferença e/ou o Sub-Total
sub_total = num_1 - num_2

# Impressão
print('A diferença entre o número, dado o seu inverso é: ', sub_total)
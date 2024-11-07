# Começo
print('Um programa que leia a soma de um número com 4 dígitos:')
num = float(input('Digite aqui o número: '))

# Meio da análise
milhar = num // 1000
resto_1 = num % 1000
centena = resto_1 // 100
resto_2 = resto_1 % 100
dezena = resto_2 // 10
unidade = resto_2 % 10

# Calcular a soma entre eles
soma = milhar + centena + dezena + unidade

# Impressão
print('O somatório dos 4 dígitos é: ', soma)
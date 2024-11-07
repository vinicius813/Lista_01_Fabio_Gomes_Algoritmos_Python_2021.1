# Intro
print('A conversão de um nibble(4 dígitos binários) em base decimal:')
num_binario = float(input('Escreva o número em base binária: '))

# Meio da questão
milhar = num_binario // 1000
resto_1 = num_binario % 1000
centena = resto_1 // 100
resto_2 = resto_1 % 100
dezena = resto_2 // 10
unidade = resto_2 % 10

# Cálculo do número binário nas suas bases
digito_1 = (2 ** 0) * unidade
digito_2 = (2 ** 1) * dezena
digito_3 = (2 ** 2) * centena
digito_4 = (2 ** 3) * milhar
digitos_totais = digito_1 + digito_2 + digito_3 + digito_4

# Valor de saída
print('A transformação de número binário para decimal é: ', digitos_totais, 'em decimal(is)')


# Entrada
print('Digite um número inteiro de 3 dígitos ao contrário:')
num = int(input('Escreva o número de 3 algarismos: '))

# Processamento
centena = num // 100
resto = num % 100
dezena = resto // 10
unidade = resto % 10

# Fim da questão
print('A inversão de seus algarismos é: ', unidade, dezena, centena, sep ='')
# Dados de entrada
print('Calcular a quantidade de dinheiro gasta por um fumante:')
print('Considere uma carteira já com 20 cigarros:')
anos = int(input('Anos gastos fumando: '))
dia_cigarros = int(input('O número de cigarros fumados por dia: '))
preco_carteira = float(input('O preço de uma carteira de cigarros é: R$'))

# Dados do processamento
anos_de_fumo = anos * 365
dinheiro_gasto = ((anos_de_fumo * dia_cigarros / 20)) * preco_carteira

# Dados finais
print('O dinheiro gasto total por um fumante será: R$', dinheiro_gasto, 'reais')
print('Atenção: fumar causa câncer de pulmão.')


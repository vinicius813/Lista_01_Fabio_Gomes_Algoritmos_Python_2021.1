# Entrada de dados
print('Leia uma questão que analisa o custo para se adquirir um carro novo:')
print('O preço do carro é em cima dos impostos.')
custo_fabrica = int(input('Digite aqui o valor de custo inicial para o comprador: '))

# Processamento de dados
preco_inicial = (custo_fabrica * 0.28) - custo_fabrica
preco_consumidor_final = (preco_inicial * 0.45) - preco_inicial

# Impressão
print('O valor final do carro novo será: R$', preco_consumidor_final)

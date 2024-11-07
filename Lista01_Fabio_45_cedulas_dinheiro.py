# Entrada
print('Um programa que receba o Algoritmo da distribuição ótima:')
print('Sabendo que no caixa disponibiliza notas de 50, 10, 5 e 1.')
saque = int(input('Digite aqui o valor em dinheiro: '))

# Processamento
notas_50 = (saque // 50) * 1
resto_1 = saque % 50
notas_10 = (resto_1 // 10) * 3
resto_2 = saque % 10
notas_5 = (resto_2 // 5) * 1
resto_3 = resto_2 % 5
notas_1 = (resto_3 * 2)

# Final da questão
print('A quantia recebida por notas de 50 será: ', notas_50)
print('A quantidade de notas de 10 será: ', notas_10)
print('A quantidade de notas de 5 será: ', notas_5)
print('A quantidade de notas de 1 real será: ', notas_1)

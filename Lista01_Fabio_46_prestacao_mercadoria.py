# Entrada
print('Questão sobre o valor de uma mercadoria mais as suas 3 prestações.')
print('Considere a entrada maior ou igual a duas últimas, sendo as mais inteiras possíveis.')

# Cálculo de parcelas
valor_mercadoria = float(input('Digite aqui o valor: '))

# Cálculo da conversão
preco_inicial = (valor_mercadoria // 3) + valor_mercadoria % 3
parcelas_divisao = (valor_mercadoria - preco_inicial) // 2

# Fim
print('O valor da prestação inicial é: ', preco_inicial)
print('O valor total, somado às 2 últimas prestações é: ', parcelas_divisao)
# Estabelecendo partes
print('Leitura de 2 frações e a respectiva soma das frações:')
numerador_1 = int(input('Digite o numerador de uma fração 1: '))
denominador_1 = int(input('Digite o denominador de uma fração 1: '))
numerador_2 = int(input('Digite o numerador da fração 2: '))
denominador_2 = int(input('Digite o denominador da fração 2: '))

# Calculando as partes das frações
denominador_x = denominador_1 * denominador_2
numerador_3 = int((denominador_x / denominador_1) * numerador_1)
numerador_4 = int((denominador_x / denominador_2) * numerador_2)
numerador_x = numerador_3 + numerador_4

# Saída
print('A soma das 2 frações será: ', numerador_x, '/', denominador_x, sep='')
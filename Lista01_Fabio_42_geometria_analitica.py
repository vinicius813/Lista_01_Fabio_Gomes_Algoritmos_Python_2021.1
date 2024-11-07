# Importando a função matemática
from math import sqrt

# Inserindo dados num plano
x1 = float(input('Digite aqui a abscissa do ponto A: '))
x2 = float(input('Digite aqui a abscisa do Ponto B: '))
y1 = float(input('Digite aqui ordenada do ponto A: '))
y2 = float(input('Digite aqui a ordenada do ponto B: '))

# Meio da questão com 2 entradas
print('A distância de dois pontos quaisquer em um plano é:')
pontos_medida = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)


# Impressão
print('A menor distância de dois pontos em um plano é: ', pontos_medida)


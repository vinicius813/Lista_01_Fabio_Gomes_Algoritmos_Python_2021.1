# Começo
print('Receber notas de 3 matérias, seus pesos e calcular a média ponderada das mesmas:')
nota_1 = float(input('Digite a primerira nota: '))
peso_1 = float(input('Digite o peso dela: '))
nota_2 = float(input('Digite a segunda nota: '))
peso_2 = float(input('Digite o peso dela: '))
nota_3 = float(input('Digite a terceira nota: '))
peso_3 = float(input('Digite o peso dela: '))

# Processo
notas = (nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3)
pesos = peso_1 + peso_2 + peso_3
media_final = notas / pesos

# Fim da questão
print('Sua média ponderada é: ', media_final)
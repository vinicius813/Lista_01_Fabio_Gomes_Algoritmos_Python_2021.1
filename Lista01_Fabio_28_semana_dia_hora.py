# Introdução
print('Um programa que receba um número de horas e transforme em semanas, dia e horas:')
hora_1 = float(input('Digite aqui o número de horas: '))

# Calcule as transformações
semana = hora_1 // 168
resto = hora_1 % 168
dia = resto // 24
hora_2 = resto % 24

# Saída
print('A conversão de horas em semanas, dias e horas é: ', semana, 'semanas', dia, 'dia(s) e', hora_2, 'horas')
# Entrada de valores
print('Um programa qu leia 2 variáveis(x e y) em um sistema de equações lineares:')
a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))
d = float(input('Digite um vaor para d: '))
e = float(input('Digite um valor para e: '))
f = float(input('Digite um valor para f: '))

# Meio da análise
x = ((a * e) - (b * d)) * ((c * e) - (b * f)) / a * b
y = ((a * e) - (b * d)) * ((a * f) - (c * d)) / d * e
calculo_1 = x + y

# Fim da análise
print('A solução para a(s) equações lineares é: ', calculo_1)
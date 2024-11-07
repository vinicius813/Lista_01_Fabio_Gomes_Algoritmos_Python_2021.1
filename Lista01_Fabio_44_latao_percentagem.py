# Entrada
print('Uma questão que aborde a produção de um latão e seus componentes:')
kg_latao = float(input('Digite quantos quilogramas de latão são oferecidos: '))

# Meio
cobre = kg_latao * 0.70
zinco = kg_latao * 0.30
qnt_latao_total = (cobre + zinco)

# Saída
print('A quantidade final de cobre é: ', cobre, 'kg')
print('A quantidade final de zinco é: ', zinco, 'kg')
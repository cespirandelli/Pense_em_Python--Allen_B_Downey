import math
# 1)
r = 5
volume = ((4/3)*math.pi)*(r**3)
print(f'1) Volume da esfera {volume:.2f}')


# 2)
exemplares = 60

preco_capa_de_livro = 24.95
preco_desconto_livraria = preco_capa_de_livro * (1-0.4)

custo_transporte = 3 + (0.75* exemplares)

custo_total = (preco_desconto_livraria*exemplares) + custo_transporte
print(f'2) Custo total de atacado para {exemplares} cópias: ${custo_total:.2f}')


# 3)
horario_saida = 6 + 52/60

passo_um = (8 * 2 + ((15 * 2)/60)) #medida em minutos
passo_dois = (7 * 3 + ((12 * 3)/60)) #medida em minutos
tempo_total = passo_um + passo_dois

horario_chegada = ((tempo_total/60) + horario_saida)*60

print(f'3) Horário de chegada em casa: {horario_chegada//60:.0f}:{horario_chegada%60:.0f}')

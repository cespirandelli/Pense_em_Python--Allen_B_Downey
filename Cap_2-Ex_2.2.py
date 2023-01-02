import math
# 1) O volume de uma esfera com raio r é 4/3 π r3. Qual é o volume de uma esfera com raio 5?
r = 5
volume = ((4/3)*math.pi)*(r**3)
print(f'1) Volume da esfera {volume:.2f}')


# 2) Suponha que o preço de capa de um livro seja de R$ 24,95, mas as livrarias recebem um 
# desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para 
# cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

exemplares = 60

preco_capa_de_livro = 24.95
preco_desconto_livraria = preco_capa_de_livro * (1-0.4)

custo_transporte = 3 + (0.75* exemplares)
custo_total = (preco_desconto_livraria*exemplares) + custo_transporte

print(f'2) Custo total de atacado para {exemplares} cópias: ${custo_total:.2f}')


# 3) Se eu sair da minha casa às 6:52 e correr 1 milha a um ritmo de 8 minutos e 15 segundos,
# depois 3 milhas a um ritmo de 7 minutos e 12 segundos, qual será o meu tempo total de corrida?
# Qual será a minha hora de chegada em casa para o café da manhã?

horario_saida = 6 + 52/60

passo_um = (8 * 2 + ((15 * 2)/60)) #medida em minutos
passo_dois = (7 * 3 + ((12 * 3)/60)) #medida em minutos
tempo_total = passo_um + passo_dois

horario_chegada = ((tempo_total/60) + horario_saida)*60

print(f'3) Horário de chegada em casa: {horario_chegada//60:.0f}:{horario_chegada%60:.0f}')
# 1) Quantos segundos há em 42 minutos e 42 segundos?

minutos = 42
segundos = 42

conversor = ((minutos*60) + segundos)
print(f'{conversor} segundos')


# 2) Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetros.

kms = 10
milhas = kms * 1.61

print(milhas, "milhas")


# 3) Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio 
# (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

minutos = 42
segundos = 42 + (minutos*60)

passo_medio = milhas / segundos
print(f'{passo_medio:.5f} milhas por segundo')

velocidade_media = passo_medio * 60
print(f'Velocidade média de {velocidade_media:.5f} milhas por hora')

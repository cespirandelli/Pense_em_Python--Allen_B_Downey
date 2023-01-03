import turtle
# 1) Escreva uma função chamda square que receba um parâmetro chamado t, que é um turtle. 
#    A função deve usar o turtle para desenhar um quadrado.
#    Escreva uma chamada de função que passe bob como um argumento para o square, e então 
#    execute o programa novamente.

bob= turtle.Turtle()
def desenhar_quadrado():
    for i in range(4):
        bob.fd(200)
        bob.lt(90)
desenhar_quadrado()

def square(t):
    for curvas in range(4):
        t.fd(200)
        t.rt(90)

square(bob)

print(bob)
turtle.mainloop

# 2) Adicione outro parâmetro, chamado length, à função square. Altere o corpo para que o
#    comprimento dos lados do quadrado seja length, e então modifique a chamada de função
#    para fornecer um segundo argumento. Execute o programa novamente. Teste sua função com
#    um valor diferente para length.

# 3) Faça uma cópia da função square e mude o nome para polygon. Adicione outro parâmetro
#    chamado n e altere o corpo para que desenhe um polígono de n lados. Dica: o ângulo
#    interno de um polígono regular de n lados é 360/n graus.

# 4) Escreva uma função chamada circle que receba um turtle, t, e um raio, r, como parâmetros
#    e que desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados
#    adequados. Teste sua função com una série de valores de r.
#    Dica: descubra a circunferência de um círculo e certifique-se de que length * n = circumference.

# 5) Faça uma versão mais geral do circle chamada arc, que que receba um parâmetro adicional
#    angle, para determinar qual fração do círculo deve ser desenhada. Angle está em unidades de graus,
#    então quando angle=360, arc deve desenhar um círculo completo.
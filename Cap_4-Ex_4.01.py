# mypolygon.py
import turtle

bob= turtle.Turtle()
def desenhar_quadrado():
    for i in range(4):
        bob.fd(200)
        bob.lt(90)

desenhar_quadrado()

print(bob)

turtle.mainloop

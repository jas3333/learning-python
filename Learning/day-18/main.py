import turtle as t
import random

t.colormode(255)


theo = t.Turtle()
theo.shape("turtle")
theo.pensize(30)
count = 0
num = -300 
theo.penup()
theo.setx(-900)
theo.speed("fastest")
theo.sety(num)


for _ in range(720):
    count += 1
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    theo.pencolor(r, g, b)
    theo.forward(1)
    theo.penup()
    theo.forward(35)
    theo.pendown()
    if count == 45:
        num += 40
        theo.penup()
        theo.sety(num)
        theo.setx(-900)
        theo.pendown()
        count = 0


screen = t.Screen()
screen.exitonclick()

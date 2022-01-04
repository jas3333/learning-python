from turtle import Turtle, Screen

theo = Turtle()
screen = Screen()
theo.shapesize(5)
theo.pensize(10)


def move_forward():
    theo.forward(10)


def turn_right():
    theo.right(10)


def turn_left():
    theo.left(10)


def go_back():
    theo.backward(10)


def clear_screen():
    theo.clear()
    theo.penup()
    theo.home()
    theo.pendown()


screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=go_back)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()





















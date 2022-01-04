from turtle import Turtle, Screen
import random


screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color(red, green, cyan, blue, pink, brown): ")
print(user_bet)
colors = ["red", "green", "cyan", "blue", "pink", "brown"]


turtle_list = []

x_cord = -800
y_cord = -200

for turtles in range(0, 6): 
    theo = Turtle(shape="turtle") 
    theo.penup()
    theo.shapesize(3)
    theo.color(colors[turtles])
    theo.goto(x_cord, y_cord)
    y_cord += 80
    turtle_list.append(theo)


if user_bet:
    keep_going = True

while keep_going:

    for turtle in turtle_list:

        if turtle.xcor() > 900:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Your {winning_turtle} turtle won!")
                keep_going = False
                break
            else:
                print(f"The {winning_turtle} turtle won, your turtle is a loser.")
                keep_going = False

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()


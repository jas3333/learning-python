from turtle import Turtle, Screen
from game import TimmyTurtle, Cars, LevelBoard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)


tim = TimmyTurtle()
level = LevelBoard()
car = Cars()
screen.listen()
screen.onkey(tim.go_up, "Up")
screen.onkey(tim.go_up, "k")

game = True

while game:
    screen.update()
    car.move()

    # Try not to make more than 50 cars
    if len(car.car_list) < 50:
        car.create_cars()

    # Check if timmy got hit
    for cars in car.car_list:
        if tim.distance(cars) < 30:
            level.display_text(0, 0, "Game Over!") 
            game = False
    
    # See if timmy made it
    if tim.ycor() > 300:
        tim.levelup()
        car.car_speed += .1
        level.update_level()


screen.exitonclick()
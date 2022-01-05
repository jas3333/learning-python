from turtle import Turtle 
import random

class TimmyTurtle(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("green")
        self.shapesize(2)
        self.penup()
        self.left(90)
        self.goto(0, -275)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


    def levelup(self):
        self.goto(0, -275)


COLORS = ["red", "brown", "green", "orange", "pink", "blue"]

class Cars():

    def __init__(self):
        self.car_list = []
        self.car_speed = .1
        self.game_start()

       
    def car_factory(self, x, y):
        random_color = random.randint(0, len(COLORS) - 1)

        car = Turtle()
        car.shape("square")
        car.color(COLORS[random_color])
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(x, y)

        # Try to separate the cars a bit
        for cars in self.car_list:
            if car.distance(cars) < 50:
                car.goto(car.xcor() + 100, car.ycor() + 100)

        self.car_list.append(car)


    # Have some cars start off in the play area
    def game_start(self):
        for cars in range(10):
            random_x = random.randint(-340, 340)
            random_y = random.randint(-200, 200)
            self.car_factory(random_x, random_y)


    # Create cars off screen for continuous traffic
    def create_cars(self):
        random_x = random.randint(600, 1500)
        random_y = random.randint(-200, 200)
        self.car_factory(random_x, random_y)


    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed 
            car.goto(new_x, car.ycor())
        self.remove_cars()

    # Delete the cars if they go off screen
    def remove_cars(self):
        for car in self.car_list:
            if car.xcor() < -450:
                car.hideturtle()
                car.clear()
                self.car_list.remove(car)


class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 0
        self.display_text(x=-300, y=220, text = f"Level: {self.level}")


    def display_text(self, x, y, text):
        self.clear()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(text, False, align="center", font=("Hack", 30, "normal"))

    def update_level(self):
        self.level += 1
        self.display_text(x=-300, y=220, text = f"Level: {self.level}")



                
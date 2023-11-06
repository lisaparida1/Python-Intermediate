from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
import random


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()
        self.MOVE_INCREMENT = 10

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_len=3, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        y_co = random.randint(-220, 220)
        new_car.goto(x=280, y=y_co)
        self.cars.append(new_car)

    def move_car(self):
        for move in self.cars:
            move.forward(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        self.MOVE_INCREMENT = self.MOVE_INCREMENT * 0.9

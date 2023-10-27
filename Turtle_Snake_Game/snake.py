from turtle import Turtle
x_cordinate = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_snaky = []
        self.create_snake()
        self.head = self.all_snaky[0]

    def create_snake(self):
        for position in x_cordinate:
            self.add_new_snaky(position)


    def add_new_snaky(self, position):
        snaky_new = Turtle(shape="square")
        snaky_new.color("white")
        snaky_new.penup()
        snaky_new.goto(position)
        self.all_snaky.append(snaky_new)

    def extend(self):
        self.add_new_snaky(self.all_snaky[-1].position())

    def move(self):
        for snakes in range(len(self.all_snaky) - 1, 0, -1):
            xcor = self.all_snaky[snakes - 1].xcor()
            ycor = self.all_snaky[snakes - 1].ycor()
            self.all_snaky[snakes].goto(x=xcor, y=ycor)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
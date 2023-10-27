from turtle import Turtle
distance = 20


class Sidebar(Turtle):

    def __init__(self, cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(cor)

    def up(self):
        self.setheading(90)
        self.forward(distance)

    def down(self):
        self.setheading(270)
        self.forward(distance)
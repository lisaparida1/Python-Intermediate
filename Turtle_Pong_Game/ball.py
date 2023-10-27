from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_co = 10
        self.y_co = 10
        self.ball_speed = 0.1

    def reset_score(self):
        self.goto(0, 0)
        self.x_co *= -1
        self.ball_speed = 0.2

    def move(self):
        xco = self.xcor() + self.x_co
        yco = self.ycor() + self.y_co
        self.goto(xco, yco)

    def bounce_y(self):
        self.y_co *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_co *= -1
        self.ball_speed *= 0.9
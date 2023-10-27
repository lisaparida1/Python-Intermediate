from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-280, y=240)
        self.level_board()

    def level_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left',  font=FONT)

    def level_increase(self):
        self.level += 1
        self.level_board()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center',  font=FONT)


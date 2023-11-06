from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color('white')
        self.penup()
        self.goto(0, 210)
        self.hideturtle()
        self.update_scoreboard()


    def get_highscore(self):
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
            return self.high_score

    def write_highscore(self, high):
        with open("highscore.txt", mode="w") as file:
            file.write(f"{high}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.write_highscore(self.score)
        self.score = 0
        self.get_highscore()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

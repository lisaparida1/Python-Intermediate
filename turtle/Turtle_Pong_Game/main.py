from turtle import Screen
from sidebar import Sidebar
from ball import Ball
from scoreboard import ScoreBoard
import time

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor('black')
scr.title("Pong Game")
scr.tracer(0)
is_true = True


right_bar = Sidebar((350, 0))
left_bar = Sidebar((-350, 0))
pong_ball = Ball()
pong_score = ScoreBoard()

scr.listen()
scr.onkey(right_bar.up, 'Up')
scr.onkey(right_bar.down, 'Down')
scr.onkey(left_bar.up, 'q')
scr.onkey(left_bar.down, 'a')

while is_true:
    time.sleep(pong_ball.ball_speed)
    scr.update()
    pong_ball.move()

    # Detects collision with top and bottom

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # Detects collision with bar

    if pong_ball.distance(right_bar) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(left_bar) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # Detects collision with walls

    if pong_ball.xcor() > 350:
        pong_ball.reset_score()
        pong_score.left_update()

    if pong_ball.xcor() < -350:
        pong_ball.reset_score()
        pong_score.right_update()

scr.exitonclick()
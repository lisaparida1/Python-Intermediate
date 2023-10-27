from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

scr = Screen()
scr.setup(width=500, height=500)
scr.bgcolor("black")
scr.title("SNAKE FOOD GAME")
scr.tracer(0)

is_true = True

snake = Snake()
food_snake = Food()
score_snake = ScoreBoard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

while is_true:
    scr.update()
    time.sleep(0.5)
    snake.move()

    #Detects collition of snake with food

    if snake.head.distance(food_snake) < 15:
        food_snake.refresh()
        snake.extend()
        score_snake.increase_score()

    #Detects collition of snake with wall

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        is_true = False
        score_snake.gameover()

    #Detects collition of snake with tail

    for snakes in snake.all_snaky[1:]:
        if snake.head.distance(snakes) < 10:
            is_true = False
            score_snake.gameover()

scr.exitonclick()
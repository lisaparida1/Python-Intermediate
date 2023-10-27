import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

play = Player()
car = CarManager()
levels = Scoreboard()

screen.listen()
screen.onkey(play.move_player, "Up")

game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    car.move_car()
    if count % 6 == 0:
        car.create_car()

    if play.ycor() > 225:
        play.reset_game()
        levels.level_increase()
        car.speed_increase()

    for carss in car.cars:
        if play.distance(carss) < 20:
            game_is_on = False
            levels.gameover()

screen.exitonclick()
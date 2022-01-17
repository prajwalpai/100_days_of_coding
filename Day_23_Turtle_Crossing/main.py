import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
game_is_on = True
screen = Screen()
screen.title("The Turtle Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_up, "Up")

list_of_cars = []
loop_count=0
while game_is_on:
    loop_count += 1
    if loop_count == 6:
        new_car = CarManager()
        list_of_cars.append(new_car)
        loop_count = 0

    time.sleep(0.1)
    screen.update()

    if player.ycor() >= 280:
        scoreboard.levelup()
        player.reset_postion()

    for car in list_of_cars:
        car.move()
        if player.distance(car) < 25:
            scoreboard.gameover()
            player.reset_postion()
            screen.update()
            time.sleep(4)
            game_is_on = False



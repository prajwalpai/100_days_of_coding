import snake
import time
import food

from turtle import Turtle, Screen

screen=Screen()
screen.title("The Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.update()

snake = snake.Snake()
food = food.Food()

screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.update()
screen.onkey(snake.down, "Down")
screen.update()
screen.onkey(snake.left, "Left")
screen.update()
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()


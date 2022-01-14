from turtle import Turtle, Screen
import generate_colors
import random

tim = Turtle()

list_of_colors = generate_colors.list_of_colors
screen = Screen()
screen.colormode(255)
tim.up()
tim.hideturtle()
loop = 10
xaxs=-250
yaxs=-250
tim.goto(xaxs,yaxs)
while loop>0:
    for _ in range(10):
        tim.dot(20, random.choice(list_of_colors))
        tim.forward(50)

    yaxs = yaxs + 50
    tim.goto(xaxs,yaxs)
    loop -= 1





screen.exitonclick()
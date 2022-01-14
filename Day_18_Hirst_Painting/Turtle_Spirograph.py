from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('deep pink')
tim.circle(100)
for angle in range(0,100,10):
    tim.circle(100,10)


screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('deep pink')
tim.penup()
tim.left(90)
tim.forward(450)
tim.left(90)
tim.forward(50)
tim.right(90)
tim.right(90)
tim.pendown()
for side in range(3,30):
    angle=360/side
    tup = (random.random(), random.random(), random.random())
    tim.pencolor(tup)

    for _ in range(side):
        tim.forward(100)
        tim.right(angle)


screen = Screen()
screen.exitonclick()
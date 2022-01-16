import time
from turtle import Turtle, Screen
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake():
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        xax = 0
        yax = 0
        for _ in range(3):
            snake = Turtle(shape='square')
            snake.penup()
            snake.pencolor('white')
            snake.fillcolor('white')
            snake.goto(xax, yax)
            xax -= 20
            self.full_snake.append(snake)


    def move(self):
        xax = 0
        yax = 0
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            xax = self.full_snake[seg_num - 1].xcor()
            yax = self.full_snake[seg_num - 1].ycor()
            self.full_snake[seg_num].goto(xax, yax)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

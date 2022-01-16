from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.fillcolor('red')
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
            xpos = self.xcor()
            ypos = self.ycor()
            self.goto(xpos+self.xmove, ypos+self.ymove)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

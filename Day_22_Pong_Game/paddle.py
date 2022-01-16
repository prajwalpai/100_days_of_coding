from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.fillcolor('yellow')
        self.goto(x, 0)


    def paddle_up(self):
        xpos = self.xcor()
        ypos = self.ycor()
        if ypos+20 < 265:
            self.goto(xpos, ypos+20)

    def paddle_down(self):
        xpos = self.xcor()
        ypos = self.ycor()
        if (ypos - 20) > -260:
            self.goto(xpos, ypos - 20)
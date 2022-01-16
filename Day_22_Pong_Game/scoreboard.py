from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scroreboard()


    def update_scroreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.lscore, align='center', font=("Courier", 80, "normal"))
        self.goto(150, 200)
        self.write(self.rscore, align='center', font=("Courier", 80, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.update_scroreboard()

    def rpoint(self):
        self.rscore += 1
        self.update_scroreboard()

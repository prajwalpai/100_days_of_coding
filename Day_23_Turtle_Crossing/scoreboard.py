from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color('black')
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-300, 250)
        self.write("Level: ", align='center', font=("Courier", 30, "normal"))
        self.goto(-220, 250)
        self.write(self.level, align='center', font=("Courier", 30, "normal"))

    def levelup(self):
        self.level += 1
        self.update_score()

    def gameover(self):
        self.level = 0
        self.update_score()
        self.goto(0,0)
        self.write('Game Over', align='center', font=("Courier", 30, "normal"))


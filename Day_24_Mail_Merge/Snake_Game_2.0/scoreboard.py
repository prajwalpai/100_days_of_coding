from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open("high_score.txt") as high:
            self.highscore = int(high.read())
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode='w') as high:
                high.write(str(self.highscore))
        self.score = 0
        self.goto(0, 0)
        self.update_scoreboard()
        #self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

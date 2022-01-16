import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.title('The Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')

l_pad = Paddle(-350)
r_pad = Paddle(350)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_pad.paddle_up, "Up")
screen.onkey(r_pad.paddle_down, "Down")
screen.onkey(l_pad.paddle_up, "w")
screen.onkey(l_pad.paddle_down, "s")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    ball.move()
#Collison with the Wall
    if 280 < ball.ycor() or ball.ycor() < -275:
        ball.bounce_y()
#Collision with the Paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 325:
        ball.bounce_x()
    if ball.distance(l_pad) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 420:
        scoreboard.lpoint()
        ball.reset_position()
        time.sleep(1)

    if ball.xcor() < -420:
        scoreboard.rpoint()
        ball.reset_position()
        time.sleep(1)

screen.exitonclick()
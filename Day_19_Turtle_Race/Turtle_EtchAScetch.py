from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#Key Operations
# W =Forwards
# S =Backwards
# A = Counter-clockwaise
# D = Clockwise
# C = Clear

def forward():
   tim.forward(10)

def back():
   tim.back(10)

def clkwise():
    tim.left(10)

def anti_clkwise():
    tim.right(10)

def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(clkwise, "d")
screen.onkey(anti_clkwise, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()

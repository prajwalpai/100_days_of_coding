import turtle

import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US State Names")
turtle.shape(image)
turtle.penup()
screen.tracer(0)
screen.setup(width=725, height=421)
df = pandas.read_csv("50_states.csv")
remaining_states = 50

while remaining_states:
    identified_num = 50 - remaining_states
    select_state = screen.textinput(title=f"({identified_num}/{remaining_states})Guess a State: ", prompt=f"Enter a state name : ").title()
    if select_state in list(df["state"]):
        remaining_states -= 1
        xpos = df[df["state"] == select_state].values[0][1]
        ypos = df[df["state"] == select_state].values[0][2]
        turtle.goto(xpos,ypos)
        turtle.write(select_state, align='center', font=("Courier", 8, "normal"))
        turtle.goto(0,0)
        screen.update()

    if remaining_states == 0:
        screen.clear()
        turtle.write("Congratulations! \n   GAME OVER", align='center', font=("Courier", 30, "normal"))
        turtle.hideturtle()


    if select_state == "Exit":
        break

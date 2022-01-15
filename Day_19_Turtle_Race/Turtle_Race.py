import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,500)
screen.colormode(255)
#list_of_colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple']
list_of_colors = ['red', 'yellow', 'blue', 'green', 'maroon', 'pink', 'orange', 'black']

#Create Turtles
list_of_turtles=[]

xaxs=-250
yaxs=-200


winner_predicted = screen.textinput(prompt=f"The Choices \n{list_of_colors} ",title="Guess the Winner")
print(f"Prediction\t : {winner_predicted}")
for i in range(8):
    list_of_turtles.append(Turtle(shape='turtle'))
    list_of_turtles[i].color(list_of_colors[i])
    list_of_turtles[i].up()
    list_of_turtles[i].goto(xaxs,yaxs)
    yaxs = yaxs + 60

turtle_temp = Turtle()
turtle_temp.up()
turtle_temp.goto(240,-270)
turtle_temp.left(90)
turtle_temp.down()
turtle_temp.forward(590)
turtle_temp.up()

if winner_predicted:
    race_is_on = True

while race_is_on:
    for turtl in list_of_turtles:
        if turtl.xcor() > 220:
            race_is_on = False
            print(f"Winner\t : {turtl.pencolor()}")
            if turtl.pencolor() == winner_predicted:
                print("You were correct")
            else:
                print("Sorry you Lost!! ")
        turtl.forward(random.randint(0,10))

screen.exitonclick()
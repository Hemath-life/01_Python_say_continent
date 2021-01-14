import turtle
import pandas
from time import sleep

screen = turtle.Screen()
# print(turtle.screensize())  # check the screensize by default
screen.title("Continent Game")
turtle.screensize(bg="black")
image = "world-map-without-labels_295105.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./continent_names.csv")
all_contenets = data.continent.to_list()

def check(answer):
    sleep(1)
    global data, all_contenets
    if answer in all_contenets:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("orange")
        state_data = data[data.continent == answer]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(arg=answer, font=("Arial", 25, "normal"))

game_on = 1

while game_on <= 10:
    answer = screen.textinput(
        title="Guess the Continent", prompt="Enter Continent name ?"
    )
    check(answer)
    game_on += 1


turtle.mainloop()

import turtle

screen = turtle.Screen()
# print(turtle.screensize())  # check the screensize by default
screen.title("Continent Game")
turtle.screensize(bg="black")
image = "world-map-without-labels_295105.gif"
screen.addshape(image)
turtle.shape(image)


x = []
y = []
def get_mouse_click_coordinate(x_cor, y_cor):
    global x, y
    x.append(x_cor)
    y.append(y_cor)
    print(x_cor, y_cor)


turtle.onscreenclick(get_mouse_click_coordinate)  # event listener




screen.mainloop() # alternative for screen.exitonclick()
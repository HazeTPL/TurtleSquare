from turtle import *

def sqare(lenght, colors):
    color(colors)
    begin_fill()
    for i in range(4):
        forward(lenght)
        left(90)
    end_fill()

speed(20)
sqare(200, "black")
sqare(150, "white")
sqare(100, "lavender")
sqare(50, "black")
hideturtle()
exitonclick()
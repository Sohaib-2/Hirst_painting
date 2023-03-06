import random
import turtle

colors_list = [ (194, 160, 121), (73, 92, 124), (142, 87, 59), (141, 160, 188), (216, 209, 122), (182, 147, 162), (29, 33, 46), (56, 34, 25), (174, 159, 42), (121, 73, 92), (139, 174, 153), (78, 114, 80), (61, 31, 40), (136, 27, 18), (117, 30, 43), (183, 100, 86), (47, 59, 92), (173, 100, 115), (102, 119, 167), (34, 51, 45), (102, 155, 89), (214, 176, 190), (67, 82, 28), (216, 181, 173), (164, 208, 186), (180, 187, 212), (217, 206, 11), (49, 71, 61), (41, 78, 84), (106, 134, 145), (173, 198, 207)]
from turtle import Screen, Turtle as T

nik = T()
turtle.speed("fastest")
turtle.colormode(255)
nik.hideturtle()

y = 0
def dotted_line():
    for _ in range(10):
        nik.dot(20,random.choice(colors_list))
        nik.penup()
        nik.forward(40)
def new_line(y):
    nik.penup()
    nik.goto(0, y)
    nik.pendown()

def draw():
    dotted_line()
    new_line(y)
for _ in range(10):
    y += 40
    draw()

















my_canvas = Screen()
my_canvas.exitonclick()
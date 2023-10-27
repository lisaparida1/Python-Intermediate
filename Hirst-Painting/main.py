# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

lis = Turtle()
lis.speed("fastest")
lis.penup()
lis.hideturtle()
scr = Screen()

lis.setheading(225)
lis.forward(320)
lis.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots+1):
    lis.dot(20, random.choice(color_list))
    lis.forward(50)

    if i % 10 == 0:
        lis.setheading(90)
        lis.forward(50)
        lis.left(90)
        lis.forward(500)
        lis.right(180)



scr.exitonclick()
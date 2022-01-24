import colorgram
import turtle
from turtle import Screen
import random

# rgb_colors = []
# colors = colorgram.extract('iu-3.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(38, 38, 38), (234, 236, 12), (236, 12, 216), (73, 78, 233), (22, 108, 6), (229, 179, 8), (38, 38, 42), (43, 36, 40), (36, 42, 36), (254, 1, 1), (223, 7, 6), (187, 14, 42), (119, 106, 29), (254, 2, 4), (81, 77, 32), (51, 52, 106), (62, 64, 159), (174, 175, 96), (212, 215, 43), (130, 133, 156), (57, 109, 25), (250, 42, 6), (139, 143, 140)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed(10)
x = -300.00
y = -300.00
tim.setposition(x, y)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50
    tim.setposition(x, y)

Screen().exitonclick()

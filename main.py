###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
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
# print(rgb_colors)
import turtle as t
import random

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
a = -176.78
tim.ht()
for n in range(10):
    for m in range(10):
        tim.pendown()
        chosen_color = random.choice(color_list)
        tim.color(chosen_color, chosen_color)
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
    a += 50
    tim.goto(-176.78, a)

screen = t.Screen()
screen.exitonclick()

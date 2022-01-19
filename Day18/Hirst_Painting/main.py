# import colorgram
# 
# extracted_colors = []
# colors = colorgram.extract('image.jpg', 35)
# for color in colors:
#     extracted_colors.append(color.rgb[:])
#
# # Same result with list comprehension
# extracted_colors = [(color.rgb[:]) for color in colors]
#
# print(extracted_colors)

import random
import turtle as t

LAYOUT = 10
COLOR_LIST = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39), (48, 65, 61)]


def draw_row():
    for _ in range(LAYOUT):
        tim.dot(20, random.choice(COLOR_LIST))
        tim.forward(50)


def move_up(pos):
    tim.setposition(pos["x"], pos["y"])


screen = t.Screen()
tim = t.Turtle()

screen.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()

position = {
    "x": -((LAYOUT - 1) * 50 / 2),
    "y": -((LAYOUT - 1) * 50 / 2),
}

tim.setposition(position["x"], position["y"])

for _ in range(LAYOUT):
    draw_row()
    position["y"] += 50
    move_up(position)

screen.exitonclick()
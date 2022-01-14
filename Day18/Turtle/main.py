from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.color("green2")

# tim.forward(100)
# tim.right(90)

# Challenge #1
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# Challenge #2
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Challenge #3
# screen.colormode(255)
# for sides in range(3, 11):
#     tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)

# Challenge #4
# def set_random_direction():
#     angle = random.choice([90, 180])
#     if random.choice(["left", "right"]) == "left":
#         tim.left(angle)
#     else:
#         tim.right(angle)
# 
# 
# screen.colormode(255)
# tim.pensize(5)
# tim.speed(10)
# for _ in range(300):
#     tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     set_random_direction()
#     tim.forward(25)

# Set random colors using RGB
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# 
# screen.colormode(255)
# directions = [0, 90, 180, 270]
# tim.pensize(5)
# tim.speed("fastest")
# 
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(25)
#     tim.setheading(random.choice(directions))

# Challenge #5

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed(0)
screen.colormode(255)

for angle in range(0, 360, 5):
    tim.pencolor(random_color())
    tim.setheading(angle)
    tim.circle(100)

screen.exitonclick()


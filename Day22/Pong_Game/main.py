from turtle import Turtle, Screen

DISTANCE = 20


def move_up():
    paddle.sety(paddle.ycor() + DISTANCE)


def move_down():
    paddle.sety(paddle.ycor() - DISTANCE)


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.turtlesize(stretch_wid=5, stretch_len=1)
paddle.setx(350)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    
    # Detect collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
    
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.refresh()
    
    screen.update()

screen.exitonclick()
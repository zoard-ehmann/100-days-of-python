# Create the screen
    # Create divider class
        # Divide the screen into 2 fields by a dashed line
# Create paddle class
    # User paddle
        # Move the paddle
    # Opponent paddle
        # Moves back and forth from top to bottom
# Create ball class
    # Spawn ball in center
    # Move ball wihin box
        # Detect collision with wall and bounce
        # Detect collision with paddle
        # Detect when paddle misses
# Create scoreboard class
    # Keep score
    
from turtle import Turtle, Screen
from divider import Divider
from paddle import Paddle
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

divider = Divider()
user_paddle = Paddle()
computer_paddle = Paddle()

user_paddle.set_start_position(-370)
computer_paddle.set_start_position(370)

screen.onkey(fun=user_paddle.move_up, key="Up")
screen.onkey(fun=user_paddle.move_down, key="Down")

is_on = True
while is_on:
    computer_paddle.move_down()
    time.sleep(.1)
    screen.update()


screen.exitonclick()
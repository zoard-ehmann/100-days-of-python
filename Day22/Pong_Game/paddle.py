from turtle import Turtle

DISTANCE = 20

class Paddle(Turtle):
    
    
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setx(x_pos)
        

    def move_up(self):
        self.sety(self.ycor() + DISTANCE)


    def move_down(self):
        self.sety(self.ycor() - DISTANCE)
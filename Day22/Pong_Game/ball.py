from turtle import Turtle

BALL_SPEED = .03

class Ball(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(1)
        self.shape("circle")
        self.color("white")
        
    
    def move(self):
        self.goto(self.position() + (BALL_SPEED, BALL_SPEED))
        
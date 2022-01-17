from turtle import Turtle

BALL_SPEED = .03

class Ball(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(1)
        self.shape("circle")
        self.color("white")
        self.x_speed = BALL_SPEED
        self.y_speed = BALL_SPEED
        
    
    def move(self):
        self.goto(self.position() + (self.x_speed, self.y_speed))
        
        
    def change_direction(self):
        self.y_speed *= -1
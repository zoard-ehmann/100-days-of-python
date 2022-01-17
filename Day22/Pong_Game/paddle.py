from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.segments = []
        self.__construct_paddle()
        
        
    def __construct_paddle(self):
        for position in range(-40, 40, 20):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.sety(position)
            self.segments.append(segment)
            
    
    def set_start_position(self, start_x):
        for segment in self.segments:
            segment.setx(start_x)
            
            
    def move_up(self):
        if self.segments[-1].ycor() < 280:
            for segment in self.segments:
                segment.sety(segment.ycor() + MOVE_DISTANCE)
            
    
    def move_down(self):
        if self.segments[0].ycor() > -280:
            for segment in self.segments:
                segment.sety(segment.ycor() - MOVE_DISTANCE)
            
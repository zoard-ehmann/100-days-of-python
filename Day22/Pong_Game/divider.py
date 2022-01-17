from turtle import Turtle

class Divider(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(-300)
        self.setheading(90)
        self.pensize(5)
        self.__draw_line()
        
    
    def __draw_line(self):
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
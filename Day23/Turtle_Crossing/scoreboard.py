from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220, 260)
        self.__write_output()
        
        
    def __write_output(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", (FONT))

    
    def increase_level(self):
        self.level += 1
        self.__write_output()
        
        
    def reset_level(self):
        self.level = 1
        self.__write_output()

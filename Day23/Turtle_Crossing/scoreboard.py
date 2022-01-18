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
        self.__output_score()
        
        
    def __output_score(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", (FONT))

    
    def increase_level(self):
        self.level += 1
        self.__output_score()
        
        
    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", (FONT))

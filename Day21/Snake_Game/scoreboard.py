from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.color("white")
        self.score = 0
        self.refresh()
        
        
    def refresh(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    
    def increment_score(self):
        self.clear()
        self.score += 1
        self.refresh()
        
        
    def game_over(self):
        self.sety(0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
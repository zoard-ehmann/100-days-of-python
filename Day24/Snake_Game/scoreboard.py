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
        self.high_score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        
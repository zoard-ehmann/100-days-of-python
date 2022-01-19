from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
HIGH_SCORE_DATA = "./Day24/Snake_Game/data.txt"

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.color("white")
        self.score = 0
        self.manage_high_score("r")
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    def reset(self):
        if self.score > self.high_score:
            self.manage_high_score("w")
        self.score = 0
        self.manage_high_score("r")
        self.update_scoreboard()
        
        
    def manage_high_score(self, action):
        with open(HIGH_SCORE_DATA, mode=action) as data:
            if action == "r":
                self.high_score = int(data.read())
            elif action == "w":
                data.write(str(self.score))
        
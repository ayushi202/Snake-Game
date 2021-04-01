from turtle import *
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.won=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.showscore()

    def showscore(self):
        self.write(f"Score : {self.won}", align="center",font=("Arial",18,"normal"))

    def update(self):
        self.won+=1
        self.clear()
        self.showscore()
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",30,"normal"))

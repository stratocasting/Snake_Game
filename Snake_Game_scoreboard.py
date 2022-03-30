from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(arg=f"score = {self.score}", move=False, align="center", font=("Arial", 8, "normal"))

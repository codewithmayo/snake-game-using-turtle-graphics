from turtle import Turtle
highest_score = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def save_high_score(self):
        with open(highest_score, "w") as file:
            file.write(str(self.high_score))

    def get_high_score(self):
        with open(highest_score, "r") as file:
            high_score_ever = file.read()
            self.high_score = int(high_score_ever)






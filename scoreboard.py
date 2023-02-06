from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = "center", font = ("Arial", 24, "normal"))


    def reset(self):
        self.clear()
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = "center", font = ("Arial", 24, "normal"))


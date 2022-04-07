from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def update_high_score(score):
    with open("score.txt", mode="w") as f:
        f.write(f"{score}")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.retrieve_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        update_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def retrieve_high_score(self):
        with open("score.txt") as f:
            self.high_score = int(f.read())
        return self.high_score

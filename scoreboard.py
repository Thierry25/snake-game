from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def increment_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

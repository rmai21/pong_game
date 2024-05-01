from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def left_point(self):
        self.l_score += 1
        self.update()

    def right_point(self):
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 60, "bold"))

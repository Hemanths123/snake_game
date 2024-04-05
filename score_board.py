from turtle import Turtle


class Score(Turtle):
    count = 0

    def __init__(self):
        super().__init__()
        self.high_score = self.read_high_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.count} High Score : {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def scores(self):
        self.count += 1
        self.clear()
        self.write(f"Score : {self.count} High Score : {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def reset_score(self):
        if self.count > self.high_score:
            self.high_score = self.count
        self.count = 0
        self.clear()
        self.write(f"Score : {self.count} High Score : {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 24, 'normal'))

    def read_high_score(self):
        file = open('high_score.txt', 'r')
        return int(file.read())

    def write_high_score(self):
        file = open('high_score.txt', 'w')
        file.write(str(self.high_score))
        file.close()

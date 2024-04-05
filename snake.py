from turtle import Turtle, Screen

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:
    def __init__(self):

        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):

        for i in positions:
            self.add_segments(i)

    def add_segments(self, i):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.goto(i)
        self.snake_segments.append(tim)

    def extend(self):
        self.add_segments(self.snake_segments[-1].position())

    def move(self):
        for i in range(len(self.snake_segments)-1, 0, -1):
            x1 = self.snake_segments[i - 1].xcor()
            y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(x1, y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def reset(self):
        for i in self.snake_segments:
            i.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
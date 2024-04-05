from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()



screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.scores()
        snake.extend()
        food.more_food()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        score.write_high_score()
        snake.reset()

    for i in snake.snake_segments[1::]:

        if snake.head.distance(i) < 10:
            score.reset_score()
            score.write_high_score()



screen.exitonclick()
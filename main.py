from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(False)

snakes = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snakes.move()

    if snakes.head.distance(food) < 20:
        food.refresh()
        snakes.extend()
        board.clear()
        board.increase_score()
        board.update_scoreboard()

    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        board.clear()
        board.reset()
        snakes.reset()

    for segment in snakes.snake_segments[1::]:
        if snakes.head.distance(segment) < 10:
            board.clear()
            board.reset()
            snakes.reset()

screen.exitonclick()
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

snakes = Snake()

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





























screen.exitonclick()
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()  # from turtle
screen.setup(width=600, height=600)  # creating size of screen
screen.bgcolor("black")  # creating back screen color
screen.title("Welcome to Snake game!")  # creating title game on the top screen
screen.tracer(0)   # update snake moves

""" my files """
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""control"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # keep  show the snake while game is on
    time.sleep(0.1)  # speed control
    snake.move()

    """ success condition - at the time touch the food, food refresh & extend snake size & increase the score  """
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    """ fail condition - touch the wall (sizes are x & y 300+ 300- )   """
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.resaet()
        snake.reset()

    """ fail condition - while touch himself """
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            scoreboard.resaet()
            snake.reset()


screen.exitonclick()

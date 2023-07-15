from scoreboard import ScoreBoard
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import random
import time

WIDTH = 800
HEIGHT = 600

# Initializing the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Initializing everything else
score = ScoreBoard()
color = 0
decreasing = True
score_count = 0
high_score = 0
random_color = (100, color, color)
snake = Snake(random_color)
food = Food(random_color)

# Measurement
WALL = WIDTH/2 - snake.snake_size() + 5
FLOOR = HEIGHT/2 - snake.snake_size() + 10

# Movement
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

border = Turtle()
border.color('white')
border.shape('square')
border.shapesize(0.1, 200)
border.penup()
border.goto(0, 255)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Checks if snake reaches a food item
    if snake.head.distance(food) < 36:
        snake.extend(random_color)
        random_color = (100, color, color)
        if color < 250 and not decreasing:
            color += 5
        elif 0 < color <= 250:
            color -= 5
            decreasing = True
        elif color == 0:
            color += 5
            decreasing = False
        food.refresh(random_color)
        score.increase_score()

    # Checks if snake hits a wall
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > 240 or snake.head.ycor() < -FLOOR:
        snake.reset(random_color)
        food.refresh(random_color)
        score.reset()

    # Checks if snake's head hits its tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            snake.reset(random_color)
            food.refresh(random_color)
            score.reset()


screen.exitonclick()




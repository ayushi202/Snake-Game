from turtle import *
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=600)
screen.title("Snake Game")
screen.tracer(0)

turtle=Turtle()
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extent()
        score.update()
        

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.gameover()
        is_game_on=False

    for j in snake.segment:
        if j!=snake.head:
            if snake.head.distance(j)<10:
                score.gameover()
                is_game_on=False

screen.exitonclick()
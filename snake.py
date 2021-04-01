from turtle import *
import time

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for i in range(0,41,20):
            snake=Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(-i,0)
            self.segment.append(snake)
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x=self.segment[i-1].xcor()
            new_y=self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.head.forward(20)

    def add_segment(self,position):
        snake=Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)

    def extent(self):
        self.add_segment(self.segment[-1].position())


    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)



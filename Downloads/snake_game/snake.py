import random
import turtle
from turtle import Turtle
turtle.colormode(255)
STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self, random_color):
        self.size = 2
        self.decreasing = True
        self.segments = []
        self.create_snake(random_color)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def reset(self, random_color):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.size = 2
        self.create_snake(random_color)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self, random_color):
        for position in STARTING_POSITIONS:
            self.add_segment(position, random_color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20 * self.size)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def add_segment(self, position, random_color):
        new_segment = Turtle()
        new_segment.color(random_color)
        new_segment.shape('square')
        new_segment.shapesize(self.size, self.size)
        self.size -= 0.025
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, random_color):
        self.add_segment(self.segments[-1].position(), random_color)

    def snake_size(self):
        return 10 * self.size


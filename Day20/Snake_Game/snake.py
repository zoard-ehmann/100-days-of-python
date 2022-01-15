from turtle import Turtle

STARTING_POSITONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_position)
        self.segments[0].forward(MOVE_DISTANCE)

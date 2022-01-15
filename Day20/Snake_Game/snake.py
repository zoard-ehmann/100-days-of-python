from turtle import Turtle

STARTING_POSITONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]


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
        self.snake_head.forward(MOVE_DISTANCE)


    def __valid_direction(self, new_direction):
        if abs(self.snake_head.heading() - new_direction) == 180:
            return False
        return True


    def up(self):
        if self.__valid_direction(UP):
            self.snake_head.setheading(UP)


    def down(self):
        if self.__valid_direction(DOWN):
            self.snake_head.setheading(DOWN)


    def left(self):
        if self.__valid_direction(LEFT):
            self.snake_head.setheading(LEFT)


    def right(self):
        if self.__valid_direction(RIGHT):
            self.snake_head.setheading(RIGHT)

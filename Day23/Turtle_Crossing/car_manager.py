from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
NUMBER_OF_CARS = 30
SPREAD = 50


class CarManager():
    
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.generate_cars()
        self.__init_car_pos()
        
    
    def __init_car_pos(self):
        for car in self.cars:
            car.setx(random.randint(-300, 300))
    
    
    def generate_cars(self):
        while len(self.cars) < NUMBER_OF_CARS:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=320, y=round(random.randint(-250, 250) / SPREAD) * SPREAD)
            self.cars.append(car)
        
        
    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                self.cars.remove(car)
                
                
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        
    
    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE

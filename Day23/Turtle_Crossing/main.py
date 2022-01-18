from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    
    
    car_manager.generate_cars()
    car_manager.move()
    
    
    if player.reached_goal():
        car_manager.increase_speed()
        scoreboard.increase_level()
        
    
    for car in car_manager.cars:
        if player.distance(car) < 20 and car.ycor() < player.ycor() or \
           player.distance(car) < 28 and car.ycor() > player.ycor() or \
           player.distance(car) < 30 and car.ycor() == player.ycor():
            player.reset_player()
            car_manager.reset_speed()
            scoreboard.reset_level()
            
        
    
    time.sleep(.1)
    screen.update()
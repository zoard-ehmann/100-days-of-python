from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

def game():
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
        screen.update()
        
        car_manager.generate_cars()
        car_manager.move()
        
        
        if player.reached_goal():
            player.go_to_start()
            car_manager.increase_speed()
            scoreboard.increase_level()
            
        
        for car in car_manager.cars:
            if player.distance(car) < 20 and car.ycor() < player.ycor() or \
            player.distance(car) < 28 and car.ycor() > player.ycor() or \
            player.distance(car) < 30 and car.ycor() == player.ycor():
                game_is_on = False
                scoreboard.game_over()
                if screen.textinput("Restart?", "Do you want to play again? Y or N").lower() == "y":
                    screen.clear()
                    game()
        
        
        time.sleep(.1)
        
        
    screen.exitonclick()
    
game()
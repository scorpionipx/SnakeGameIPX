# SNAKE PLAYER
# SnakeGameIPX

# IMPORTED MODULES
import turtle

player_snake = None

def init_snake():
    
    #Create the player turtle
    player_snake = turtle.Turtle()

    
    player_snake.color('white')
    
    player_snake.penup()
    player_snake.speed(1)
    player_snake.setposition(0, 0)
    player_snake.setheading(90)

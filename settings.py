# SETTINGS

# SnakeGameIPX

# Imported modules
import turtle
import os
import snake
from snake import player_snake
import time

# constants - use instead of magical numbers

BACKGROUND_COLOR = 'black'
GAME_TITLE = 'SnakeGamePX'
BORDER_COLOR = 'white'
BORDER_WIDTH = 4

GAME_BORDER_LENGHT = 800
GAME_BORDER_HEIGHT = 600

SCORE_BORDER_LENGHT = 400
SCORE_BORDER_HEIGHT = 600

BORDER_DRAWING_SPEED = 0 # MAXIMUM SPEED

INIT_GAME_BORDER_POS_X = -600
INIT_GAME_BORDER_POS_Y = -300

INIT_SCORE_BORDER_POS_X = 250
INIT_SCORE_BORDER_POS_Y = -300

PLAYER_SPEED = 10

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

DIRECTION = LEFT

def init_window():

    # set up the screen (creates the window)
    wn = turtle.Screen()
    # sets background color
    wn.bgcolor(BACKGROUND_COLOR)
    # set window title
    wn.title(GAME_TITLE)
    # register shapes
    wn.register_shape('Images\snake_head.gif')

def init_game_border():
    
    # Draw game border

    # created border turtle
    border_pen = turtle.Turtle()
    # set it's speed
    border_pen.speed(BORDER_DRAWING_SPEED)
    # set it's color
    border_pen.color(BORDER_COLOR)
    # set it's width
    border_pen.pensize(BORDER_WIDTH)
    # disable drawing
    border_pen.penup()
    # set it's position
    border_pen.setposition(INIT_GAME_BORDER_POS_X, INIT_GAME_BORDER_POS_Y)
    # enable drawing
    border_pen.pendown()

    # draw the border
    border_pen.forward(GAME_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_HEIGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_HEIGHT)
    border_pen.left(90)

    # hide pen
    border_pen.hideturtle() 
    


def init_score_border():
    
    # Draw score border

    # created border turtle
    border_pen = turtle.Turtle()
    # set it's speed
    border_pen.speed(BORDER_DRAWING_SPEED)
    # set it's color
    border_pen.color(BORDER_COLOR)
    # set it's width
    border_pen.pensize(BORDER_WIDTH)
    # disable drawing
    border_pen.penup()
    # set it's position
    border_pen.setposition(INIT_SCORE_BORDER_POS_X, INIT_SCORE_BORDER_POS_Y)
    # enable drawing
    border_pen.pendown()

    # draw the border
    border_pen.forward(SCORE_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_HEIGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_HEIGHT)
    border_pen.left(90)

    # hide pen
    border_pen.hideturtle() 
    

    
def set_direction_left():
    global DIRECTION, LEFT
    DIRECTION = LEFT
        
def set_direction_right():
    global DIRECTION, RIGHT
    DIRECTION = RIGHT
    
def init_game():

    global DIRECTION
    

    init_window()
    init_game_border()
    init_score_border()
    
    #Create the player turtle
    
    player_snake = turtle.Turtle()
    
    player_snake.color('white')
    
    player_snake.penup()
    player_snake.speed(1)
    player_snake.setposition(-500, 0)
    player_snake.setheading(0)
    player_snake.shape('Images\snake_head.gif')
    player_snake.settiltangle(30)
    player_snake.tilt(30)

    
    turtle.listen()
    turtle.onkey(set_direction_left, "Left")
    turtle.onkey(set_direction_right, "Right")

    while True:
        time.sleep(.2)
        
        x = player_snake.xcor()
        if DIRECTION == LEFT:
            x -= PLAYER_SPEED
        elif DIRECTION == RIGHT:
            x += PLAYER_SPEED
        player_snake.setx(x)


init_game()

    


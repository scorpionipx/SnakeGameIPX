# SETTINGS

#GameIPX - Part 1

import turtle
import os

# constants - use instead of magical numbers

BACKGROUND_COLOR = 'black'
GAME_TITLE = 'SnakeGamePX'
BORDER_COLOR = 'white'
BORDER_WIDTH = 4

GAME_BORDER_LENGHT = 800
GAME_BORDER_HEIGHT = 600
SCORE_BORDER_LENGHT = 400
SCORE_BORDER_HEIGHT = 600

INIT_GAME_BORDER_POS_X = -600
INIT_GAME_BORDER_POS_Y = -300

INIT_SCORE_BORDER_POS_X = 250
INIT_SCORE_BORDER_POS_Y = -300

def init_window():

    # set up the screen (creates the window)
    wn = turtle.Screen()
    # sets background color
    wn.bgcolor(BACKGROUND_COLOR)
    # set window title
    wn.title(GAME_TITLE)

def init_game_border():
    
    # Draw game border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color(BORDER_COLOR)
    border_pen.penup()
    border_pen.setposition(INIT_GAME_BORDER_POS_X, INIT_GAME_BORDER_POS_Y) # ???
    border_pen.pendown()
    border_pen.pensize(BORDER_WIDTH)

    border_pen.forward(GAME_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_HEIGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(GAME_BORDER_HEIGHT)
    border_pen.left(90)
    
    border_pen.hideturtle() 
    


def init_score_border():
    
    # Draw game border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color(BORDER_COLOR)
    border_pen.penup()
    border_pen.setposition(INIT_SCORE_BORDER_POS_X, INIT_SCORE_BORDER_POS_Y) # ???
    border_pen.pendown()
    border_pen.pensize(BORDER_WIDTH)

    border_pen.forward(SCORE_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_HEIGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_LENGHT)
    border_pen.left(90) 
    border_pen.forward(SCORE_BORDER_HEIGHT)
    border_pen.left(90)
    
    border_pen.hideturtle() 
    

def init_game():

    init_window()
    init_game_border()
    init_score_border()


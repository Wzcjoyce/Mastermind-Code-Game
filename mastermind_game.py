'''
CS5001 Final Project

Zuocheng Wang

Mastermind code Game

This is the main function of the mastermind code game
'''
import random
import turtle
from mastermind_game_helper_functions import *
from mastermind_game_turtle_functions import *
from Marble import *

def main():

    # Using create_secret_code function to randomly create a secret code list.
    secret_code = create_secret_code()
    
    # Setup the initial turtle screen    
    screen = turtle.Screen()
    screen.screensize(1000 , 900)
    screen.setup(1000 , 900)
    screen.title("CS5001 Mastermind Code Game")
    turtle.hideturtle()
    turtle.tracer(2,3)
    
    # Pop-up a windown for user to input the player name.
    dialog_window = turtle.Screen()
    player_name = dialog_window.textinput("Mastermind Game","You Name:")
    
    #Draw 3 blocks for game board, leaderboard and click board.
    draw_rectangle(-470, 420, 600, 700, "black")
    draw_rectangle(180, 420, 280, 700, "blue")
    draw_rectangle(-470, -300, 930, 120, "black")
    
    turtle.update()

    # Draw the inital marbles, peges and selection marbles.
    marble_list = draw_marble_layout()
    pegs_list = draw_pegs_layout()
    marble_selection_list = draw_selection_marbles() 

    # import the checkbutton, xbutton and quit button.       
    add_gif("checkbutton.gif", 10, -375)
    add_gif("xbutton.gif", 100, -375)
    add_gif("quit.gif", 355, -360)
    
    initial_run_number = 0

    # Start the game through start_run function.
    start_run(player_name, initial_run_number, marble_list, pegs_list, marble_selection_list, secret_code)


if __name__ == "__main__":
    main()

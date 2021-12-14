'''
CS5001 Final Project

Zuocheng Wang

Mastermind code Game
Turtle helper Functions

This file include helper functions which are involved
with turtle library.
'''
import random
import turtle
import time
from Marble import *
from Point import *
from mastermind_game_helper_functions import *


def draw_rectangle(x, y, x_length, y_length, color):
    '''
    Function -- draw_rectangle
        draw rectangle using turtle
        
    Parameters:
        x -- start coordinate in x axis
        y -- start coordinate in y axis
        y -- start coordinate in y axis
        x_length -- length of rectange in x axis
        y_length -- length of rectange in y axis
        color -- color of the rectangle
        
    Return:
        No variable returned from this function
    '''
    turtle.hideturtle()

    # make turtle to draw associated color and set the pen size.
    turtle.color(color)
    turtle.pensize(6)

    turtle.penup()

    # Let the turtle go to the coordinate of the top-right corner of the rectangle
    turtle.goto(x,y)

    # Start to draw the rectangle from the top-right corner
    turtle.pendown()
    turtle.forward(x_length)
    turtle.right(90)
    turtle.forward(y_length)
    turtle.right(90)  
    turtle.forward(x_length)
    turtle.right(90)
    turtle.forward(y_length)

    turtle.penup()

    # Let turtle go back to the origin (0,0)   
    turtle.home()

    # make sure that the heading of turtle is at default
    turtle.setheading(0)

    
    

def draw_marble_layout():
    '''
    Function -- draw_mastermind_code
        draw mastermind empty code in game board (with no player selections)
        
    Parameters:
        x -- coordinate of the bottom of the first marble in x axis
        y -- coordinate of the bottom of the first marble in y axis
        y -- space between the bottom of marbles in y axis
        x_space -- space between marbles in x axis
        y_space -- space between marbles in y axis
        number_of_chance -- number of chance user can use
        
    Return:
        return a list of objects(empty marbles for player to make their guess) in Marble class
    '''
    marble_list = []    

    # i is the row number from 0 to 9 (10 allowed guesses from player)
    # j is the number of selection in each guess which is from 0 to 3 (4 selections).
    for i in range(10):      
        for j in range(4):
            
            marble = Marble(Point(-370 + 70*j,350 - 67*i), "white")
            marble.draw_empty()
            marble_list.append(marble)
            
    return marble_list


def add_gif(gif_file_name, x, y):
    '''
    Function -- add_gif
        add gif file to the game board.
        
    Parameters:
        gif_file_name -- file name of image
        x -- x coordinate of the center of the gif image
        y -- y coordinate of the center of the gif image
        
    Return:
        No variable returned from this function
    '''
    try:

        image = turtle.Turtle()
        image.penup()
        image.goto(x, y)
        turtle.addshape(gif_file_name)
        image.shape(gif_file_name)

    except:

        add_gif("file_error.gif", 0, 0)
        
   
def draw_pegs_layout():
    '''
    Function -- draw_mastermind_code
        draw blank pegs at begining of the game.
        
    Parameters:
        no parameters
        
    Return:
        return a list of objects(empty pegs marbles to show number of bulls and cows) in Marble class
    '''

    pegs_list = []
    
    # i is the run number from 0 to 9(10 guess from player)
    # j is the row number in each guess
    # k is the column number in each guess
    for i in range(10):   
        for j in range(2):
            for k in range(2):
                
                pegs = Marble(Point(-30 + 15*k,375 - 15*j - 67*i), "white", 5) # the radius of pegs is set to 5.
                pegs.draw_empty()
                pegs_list.append(pegs)

    return pegs_list


def draw_selection_marbles():
    '''
    Function -- draw_selection_marbles
        draw selection marbles in turtle for player to select their guess code.
        
    Parameters:
        no parameter
        
    Return:
        return a list of objects(selection marbles) in Marble class
    '''
    color_selection_list = ["blue", "red", "green", "yellow", "purple", "black"]

    marble_selection_list = []

    # i is the No. of marble from left to right (0 to 5)
    for i in range(6):
        
        marble_selection = Marble(Point(-430 + 60*i, -375), color_selection_list[i], 20)
        marble_selection.draw()
        marble_selection_list.append(marble_selection)

    return marble_selection_list

    
# Nested start game function which has a get_mouse_click function inside.
def start_run(player_name, run_number, marble_list, pegs_list,  marble_selection_list, secret_code):
    '''
    Function -- start_run
        This function is to initiate the whole game run which has a
        nested function get_mouse_click inside to capture player's
        mouse clicks.
        
    Parameters:
        player_name -- name of player
        run_number -- run number (number of guess player is currently in)
        marble_list -- list of marble object in Marble class
        pegs_list -- list of pegs object in Marble class
        marble_selection_list -- list of selection marble objects in Marble class
        secret_code -- secret code (correct answer) 
        
    Return:
        no return value
    '''
    turtle.hideturtle()

    # The initial game setting up( run number, selection number) 
    number_of_selection = 0
    guess_list = []
    selection = CountSelection(number_of_selection, guess_list)
    run = CountRunNumber(run_number)

    # Draw the indication arrow to indicate which run player is currently in.
    indication_arrow = Arrow(-435, 375 - 67*run.number_of_run())
    indication_arrow.draw_arrow()

    # open the leaderboard file
    leaderboard_list = open_leaderboard_file("leaderboard_file.txt")

    # This object is used to indicate that game is currently running.
    game_process = IsGameRunning(True)

    # process the information from leaderboard file and write into game board.
    player_information = LeaderBoard(player_name, 10)
    leaderboard_text = AddText(leaderboard_list, 200, 380)
    leaderboard_text.write_text()

    quit_message_image = AddResultGif("quitmsg.gif",0 ,0)
    
    def get_mouse_click(x, y):
        '''
        Function -- get_mouse_click
            This function is a nested function in start run function to capture
            player's click on the game board.
        
        Parameters:
            x -- x coordinate of player's click
            y -- y coordinate of player's click
        
        Return:
            no return value
        '''
        color_selection_list = ["blue", "red", "green", "yellow", "purple", "black"]

        # This is the coordination of Quit gif, once player click it, it will pop up a quit message
        # and exit the program.
        if (x >= 255 and x <= 455
            and y >= -416 and y <= -304):
            
            game_process.game_is_stop()
            quit_message_image.draw_gif()
            quit_message_image.show_gif()
            time.sleep(2)
            
            exit()

        # The following 6 elif conditions are the coordination of selection marbles for player to make their guesses.
        # Also, guess is captured only when game_process object is True.
        elif marble_selection_list[0].clicked_in_region(x, y) == True and game_process.status == True and "blue" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[0].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "blue")
                selection.add_selection_count()
                selection.append_guess("blue")
                
        elif marble_selection_list[1].clicked_in_region(x, y) == True and game_process.status == True and "red" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[1].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "red")
                selection.add_selection_count()
                selection.append_guess("red")
                
        elif marble_selection_list[2].clicked_in_region(x, y) == True and game_process.status == True and "green" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[2].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "green")
                selection.add_selection_count()
                selection.append_guess("green")
                
        elif marble_selection_list[3].clicked_in_region(x, y) == True and game_process.status == True and "yellow" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[3].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "yellow")
                selection.add_selection_count()
                selection.append_guess("yellow")
                
        elif marble_selection_list[4].clicked_in_region(x, y) == True and game_process.status == True and "purple" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[4].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "purple")
                selection.add_selection_count()
                selection.append_guess("purple")
                
        elif marble_selection_list[5].clicked_in_region(x, y) == True and game_process.status == True and "black" not in selection.guess_list:
            if selection.number_of_selection < 4:
                marble_selection_list[5].draw_empty()
                marble_serial_number = run.number_of_run()*4 + selection.number_of_selection
                change_marble_color(marble_list, marble_serial_number, "black")
                selection.add_selection_count()
                selection.append_guess("black")


        # Player submit their answer through clicking green check button.               
        elif (x >= -20 and x <= 40
            and y >= -405 and y <= -345) and game_process.status == True:

            # Player get the correct answer within 10 rounds.
            if selection.number_of_selection == 4:
        
                number_of_bulls, number_of_cows = count_bulls_and_cows(secret_code, selection.guess_list)
                show_result_in_pegs(pegs_list, number_of_bulls, number_of_cows, run.number_of_run())

                # When number_of_bulls equal to 4, player won the game, winner gif should be poped up
                # and game process is stop, leaderboard is updated and write the latest leaderboard into associated file.
                if number_of_bulls == 4:
                    winner_gif = AddResultGif("winner.gif", 0, 0)
                    winner_gif.draw_gif()
                    screen = turtle.Screen()
                    game_process.game_is_stop()
                    final_score = str(run.number_of_run() + 1)
                    write_score_to_leaderboard_file(player_name, final_score , "leaderboard_file.txt")
                    new_leaderboard_list = open_leaderboard_file("leaderboard_file.txt")
                    new_leaderboard_list = sort_leaderboard_list(new_leaderboard_list)
                    leaderboard_text.update_text(new_leaderboard_list)
                    

                    # allow to start next round without exit the program.
                    try_again = screen.textinput("Want to play again?","Y to play again, others to exit")

                    # If answer is no or none, exit the program.
                    if try_again == None:
                        time.sleep(3)
                        exit()

                    # If the answer is yes, then reset everything and run the start_run function again.
                    # to start the next turn.
                    elif try_again.upper() == "Y":
                        
                        turtle.tracer(2,3)
                        winner_gif.clear_gif()
                        run.reset_to_zero()
                        new_secret_code = create_secret_code()
                        print(new_secret_code)

                        for i in range(10):

                            for j in range(4):
                    
                                change_marble_color(marble_list, i*4 + j, "white")

                        for i in range(10):

                            for j in range(4):
                    
                                change_pegs_color(pegs_list, i*4 + j, "white")
                                    

                        for i in range(len(selection.guess_list)):

                            location = color_selection_list.index(selection.guess_list[i])
                            marble_selection_list[location].draw()

                        indication_arrow.clear_arrow()
                        leaderboard_text.clear_text()
                        turtle.update()
                        
                        start_run(player_name, run.number_of_run(), marble_list, pegs_list, marble_selection_list, new_secret_code)

                    # If answer is no or none, exit the program.
                    else:
                        time.sleep(3)
                        exit()

                # If the number of run is within 9, player can still guess the secret code.
                elif run.number_of_run() < 9:

                    for i in range(len(selection.guess_list)):

                        location = color_selection_list.index(selection.guess_list[i])
                        marble_selection_list[location].draw()

                    run.add_run_number()
                    indication_arrow.clear_arrow()
                    leaderboard_text.clear_text()
                    start_run(player_name, run.number_of_run(), marble_list, pegs_list, marble_selection_list, secret_code)


                # If the number of run is equal 9, player run out of their guesses.
                # Ask if player want to play next turn.
                elif run.number_of_run() == 9:

                    lose_image = AddResultGif("Lose.gif",0 ,0)
                    lose_image.draw_gif()
                    lose_image.show_gif()
                    game_process.game_is_stop()
                    screen = turtle.Screen()

                    # allow to start next round without exit the program.
                    try_again = screen.textinput("try again?","Y to play again, others to exit")

                    # If answer is no or none, exit the program.
                    if try_again == None:
                        time.sleep(3)
                        exit()
                        
                    # If the answer is yes, then reset everything and run the start_run function again.
                    # to start the next turn.    
                    elif try_again.upper() == "Y":
                        
                        turtle.tracer(2,3)
                        lose_image.clear_gif()
                        run.reset_to_zero()
                        new_secret_code = create_secret_code()

                        for i in range(10):

                            for j in range(4):
                
                                change_marble_color(marble_list, i*4 + j, "white")

                        for i in range(10):

                            for j in range(4):
                
                                change_pegs_color(marble_list, i*4 + j, "white")

                        for i in range(len(selection.guess_list)):

                            location = color_selection_list.index(selection.guess_list[i])
                            marble_selection_list[location].draw()
                    
                        leaderboard_text.clear_text()
                        indication_arrow.clear_arrow()
                        turtle.update()
                        start_run(player_name, run.number_of_run(), marble_list, pegs_list, marble_selection_list, new_secret_code)

                    # If answer is no or none, exit the program.   
                    else:
                        time.sleep(3)
                        exit()

                                              
        # When x button is clicked, remove the color in game board and restore the color marble in selection board
        # Clear the arrow and run the start_run function again.
        elif (x >= 70 and x <= 130
            and y >= -405 and y <= -345) and game_process.status == True:  
            
            for i in range(4):
                
                change_marble_color(marble_list, run.number_of_run()*4 + i, "white")

            for i in range(len(selection.guess_list)):

                location = color_selection_list.index(selection.guess_list[i])

                marble_selection_list[location].draw()

            indication_arrow.clear_arrow()
            leaderboard_text.clear_text()
            
            start_run(player_name, run.number_of_run(), marble_list, pegs_list, marble_selection_list, secret_code)


    # Start to capture the mouse click by input the get_mouse_click function above into onscreenclick turtle event.              
    turtle.onscreenclick(get_mouse_click)



def show_result_in_pegs(pegs_list, number_of_bulls, number_of_cows, run_number):
    '''
    Function -- show_result_in_pegs
        draw pegs based on number of bulls and number of cows.
        
    Parameters:
        marble_list -- list of objects in Marble class
        number_of_bulls -- number of bulls
        number_of_cows -- number of cows
        run_number -- run number (number of guesses player is currently in) 
        
    Return:
        No variable returned from this function
    '''
    pegs_location_list = [0, 1, 2, 3]

    if number_of_bulls != 0:

        for i in range(number_of_bulls):

            random_location = random.choice(pegs_location_list)
            location_index = pegs_location_list.index(random_location)
            pegs_location_list.pop(location_index)
            pegs_serial_number = run_number*4 + random_location
            change_pegs_color(pegs_list, pegs_serial_number, "black")
            
        if number_of_cows != 0:     

            for j in range(number_of_cows):
            
                random_location = random.choice(pegs_location_list)
                location_index = pegs_location_list.index(random_location)
                pegs_location_list.pop(location_index)
                pegs_serial_number = run_number*4 + random_location
                change_pegs_color(pegs_list, pegs_serial_number, "red")

    else:

        if number_of_cows != 0:

            for j in range(number_of_cows):
            
                random_location = random.choice(pegs_location_list)
                location_index = pegs_location_list.index(random_location)
                pegs_location_list.pop(location_index)
                pegs_serial_number = run_number*4 + random_location
                change_pegs_color(pegs_list, pegs_serial_number, "red")

  

def change_marble_color(marble_list, marble_serial_number, new_color):
    '''
    Function -- change_marble_color
        change the color of marble
        
    Parameters:
        marble_list -- list of objects in Marble class
        marble_serial_number -- serial number of marble in list. The color of this marble will be changed.
        new_color -- the color we want to change to.
        
    Return:
        No variable returned from this function
    '''
    round_number = marble_serial_number // 4
    column_number = marble_serial_number - round_number*4
    
    marble_list[marble_serial_number] = Marble(Point(-370 + 70*(column_number), 350 - 67*(round_number)), new_color)
    marble_list[marble_serial_number].draw()


def change_pegs_color(pegs_list, pegs_serial_number, new_color):
    '''
    Function -- change_pegs_color
        change the color of pegs marble
        
    Parameters:
        pegs_list -- list of objects in Marble class
        pegs_serial_number -- serial number of pegs in the pegs object list. The color of this pegs will be changed.
        new_color -- the color we want to change to.
        
    Return:
        No variable returned from this function
    '''
    round_number = pegs_serial_number // 4
    row_number = (pegs_serial_number - round_number*4) // 2
    column_number = pegs_serial_number - round_number*4 - row_number*2

    pegs_list[pegs_serial_number] = Marble(Point(-30 + 15*(column_number),375 - 15*(row_number) - 67*(round_number)), new_color, 5)
    pegs_list[pegs_serial_number].draw()



class Arrow:
    '''
    This Arrow class is to add Arrow to game board through turtle
    to indicate which run(guess) player is currently in. 
    '''
    def __init__(self, x, y, color="red"):
        '''
        This method is to initiate the Arrow class and save instance variables
        '''
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.x = x
        self.y = y
        self.color = color
        self.pen.speed(0)
        self.visible = False

        
    def draw_arrow(self):
        '''
        This method is to draw Arrow on the game board
        '''
        self.pen.penup()
        self.pen.goto(self.x, self.y)

        self.pen.begin_fill()
        self.pen.fillcolor(self.color)
        self.pen.pendown()
        self.pen.left(120)
        self.pen.forward(30)
        self.pen.right(150)
        self.pen.forward(51.96)
        self.pen.right(120)
        self.pen.forward(51.96)
        self.pen.right(150)
        self.pen.forward(30)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.setheading(0)
        self.visible = True

    def clear_arrow(self):
        '''
        This method is to clear Arrow on the game board
        '''
        self.pen.clear()
        


class AddText:
    '''
    This AddText class is to add text to game board through turtle.
    '''
    def __init__(self, text_list, x, y):
        '''
        This method is to initiate the AddText class and save instance variables
        '''
        self.txt = turtle.Turtle()
        self.txt.hideturtle()
        self.color = "blue"
        self.text_list = text_list
        self.x = x
        self.y = y
        self.txt.speed(0)

    def write_text(self):
        '''
        This method is to draw text on the game board
        '''
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(self.x, self.y)

        # Only show the top 3 players with their scores
        if len(self.text_list) > 4:

            leader_number = 4

        else:
            
            leader_number = len(self.text_list)


        for i in range(leader_number):
            self.txt.pendown()
            self.txt.write(f"{self.text_list[i]}",font = ("Arial", 15, "normal"))

            self.txt.penup()
            self.txt.goto(self.x, self.y - 80*(i + 1) )
            
      
    def update_text(self, new_list):
        '''
        This method is to update the text on the game board
        based on the parameter new_list.
        '''
        self.clear_text()
        self.text_list = new_list
        self.write_text()

    def clear_text(self):
        '''
        This method is to clear text on the game board
        '''
        self.txt.clear()

    
class AddResultGif:
    '''
    This AddResultGif class is to manage the gif image on the game board
    '''
    def __init__(self, gif_name, x, y):
        '''
        This method is to initiate the AddResultGif class and save instance variables
        '''
        self.gif = self.new_pen()
        self.gif_name = gif_name
        self.x = x
        self.y = y

    def new_pen(self):
        return turtle.Turtle()

    def draw_gif(self):
        '''
        This method is to import gif image to the game board
        '''
        self.gif.penup()
        self.gif.goto(self.x, self.y)
        turtle.addshape(self.gif_name )
        self.gif.shape(self.gif_name)
            

    def clear_gif(self):
        '''
        This method is to clear gif image from the game board
        '''
        self.gif.hideturtle()

    def show_gif(self):
        '''
        This method is to show gif image from the game board
        '''
        self.gif.showturtle()


def open_leaderboard_file( file ):
    '''
    Function -- open_leaderboard_file
        The functionality of function open_leaderboard_file is to
        oepn the leaderboard_file.txt and return a unsorted list.      

    Parameters:
        file -- file name
        
    Return:
        return a unsorted leaderboard list. 
    '''
    try:
        with open(file, "r") as leaderboard_txt:
            
            leaderboard_list = process_leaderboard_file( leaderboard_txt )

    except:

        # If IOError is raised, we should add error gif to the turtle.   
        leaderboard_error_image = AddResultGif("leaderboard_error.gif", 0, 0)
        leaderboard_error_image.draw_gif()
        time.sleep(2)

        # set the default value for leaderboard when there is no leaderboard_file.txt
        write_score_to_leaderboard_file("", 0, "leaderboard_file.txt")
        leaderboard_error_image.clear_gif()

        # Even if the leaderboard file cannot be open, we can return a empty list
        # to continue the game.
        leaderboard_list = []
        
        return leaderboard_list

    else:

        return leaderboard_list


def write_score_to_leaderboard_file( leader_name, score , output_file_name ):
    '''
    Function -- write_score_to_leaderboard_file
        The functionality of function write_score_to_leaderboard_file is to
        write the latest score and player name into leaderboard_file.txt        

    Parameters:
        leader_name -- player name
        score -- Associated score player get
        output_file_name -- name of the file this function write to
        
    Return:
        no return
    '''

    if leader_name != "" and score != 0:
    
        with open( output_file_name , "a") as leaderboard_result:
            leaderboard_result.write("\n")
            leaderboard_result.write(score + ": ")
            leaderboard_result.write(leader_name)

    elif leader_name == "" and score == 0:
        with open( output_file_name , "w") as leaderboard_result:
            leaderboard_result.write('Leaders:')

        leaderboard_text = AddText(['Leaders:'], 200, 380)
        leaderboard_text.write_text()

        



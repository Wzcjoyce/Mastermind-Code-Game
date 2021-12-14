'''
CS5001 Final Project

Zuocheng Wang

Mastermind code Game

helper functions

This file include helper functions which are not involved
with turtle library.
'''
import random
import turtle
import time
from Marble import *
from Point import *

def create_secret_code():
    '''
    Function -- create_secret_code()
        random create a secret code list from the colors.
        4 colors should be in the list.
        
    Parameters:
        no parameters
    
    Return:
        a random list containing 4 colors from the colors list
    '''
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black']

    secret_codes_list = []

    for i in range(4):

        secret_code = random.choice(colors)
        position_index = colors.index(secret_code)
        colors.pop(position_index) 
        secret_codes_list.append(secret_code)

    return secret_codes_list


def count_bulls_and_cows(secret_code, guess):
    '''
    Function -- count_bulls_and_cows
        count number of bulls and number of cows by comparing the input secret code list
        and the guess list.
        
    Parameters:
        secret_code -- The secret code list
        guess -- The guess list
        
    Return:
        a tuple with two elements containing the number of bulls and cows by comparing with the secret code
    '''
    number_of_bulls = 0
    number_of_cows = 0
  
    for i in range(len(secret_code)):

        for j in range(len(guess)):

            # If a color match up, number of cow plus 1.
            if guess[j] == secret_code[i]:

                number_of_cows += 1

                # If the position also match up,
                # number of cow minus 1(we have added 1 in last if condition) and number of bull plus 1.
                if i == j:

                    number_of_bulls += 1
                    number_of_cows -= 1
                    

    return number_of_bulls, number_of_cows


class CountSelection:
    '''
    This CountSelection class manages the number of selection in one player guess.
    When player click x button, this class is used to reset the number of selection to zero.
    '''
    def __init__(self, number_of_selection, guess_list):
        '''
        Method -- __init__(constructor)  
            initialization of the CountSelection class. It save the parameters.

        Parameters:
            self -- instance of the class
            number_of_selection -- number of player's selection in one guess
            guess_list -- the guess list player selected

        No variable returned from this method 
        '''
        self.number_of_selection = number_of_selection
        self.guess_list = guess_list

    def number_of_selection(self):
        '''
        Method -- number_of_selection  
            To return the current number of selection

        Parameters:
            self -- instance of the class

        Return:
            the current number of selection.
        '''
        return self.number_of_selection

    def add_selection_count(self):
        '''
        Method -- add_selection_count  
            To add 1 to the current number of selection

        Parameters:
            self -- instance of the class

        Return:
            the updated number of selection.
        '''
        self.number_of_selection = self.number_of_selection + 1

        return self.number_of_selection 


    def append_guess(self, guess_code):
        '''
        Method -- append_guess  
            To append the player's selection to the guess list

        Parameters:
            self -- instance of the class

        Return:
            the updated guess list
        '''
        temp_list = self.guess_list

        temp_list.append(guess_code)

        self.guess_list = temp_list

        return self.guess_list


    def guess_list(self):
        '''
        Method -- guess_list  
            To return the current guess_list

        Parameters:
            self -- instance of the class

        Return:
            the current guess_list.
        '''
        return self.guess_list


class CountRunNumber:
    '''
    This CountRunNumber class manages the number of runs(number of guess player have tried).
    When player click check button, this class is used to add 1 to the number of runs
    and when player click one color, this class is used to reset the number of run to zero.
    '''
    def __init__(self, run_number):
        '''
        Method -- __init__(constructor)  
            initialization of the CountRunNumber class. It save the parameters.

        Parameters:
            self -- instance of the class
            run_number -- number of runs (number of guess player have tried)

        No variable returned from this method 
        '''
        self.run_number = run_number

        if self.run_number < 0:

            raise ValueError


    def number_of_run(self):
        '''
        Method -- number_of_run  
            To return the current number of runs

        Parameters:
            self -- instance of the class

        Return:
            the current number of runs.
        '''
        return self.run_number

    def add_run_number(self):
        '''
        Method -- add_run_number  
            To add 1 to the current number of run

        Parameters:
            self -- instance of the class

        Return:
            the updated number of run.
        '''
        self.run_number = self.run_number + 1

        return self.run_number

    def reset_to_zero(self):
        '''
        Method -- add_run_number  
            To reset to the number of run to zero

        Parameters:
            self -- instance of the class

        Return:
            the updated number of run.
        '''
        self.run_number = 0

    def __str__(self):
        '''
        Method -- __str__  
            To express the instance in string

        Parameters:
            self -- instance of the class

        Return:
            no return
        '''
        return  f"{self.run_number}"


class IsGameRunning:
    '''
    This CountRunNumber class manages the status game running.
    When player win or lose, click should no longer be captured. So, I add this class to control the game runinng status. 
    '''
    def __init__(self, status):
        '''
        Method -- __init__(constructor)  
            initialization of the IsGameRunning class. It save the parameters.

        Parameters:
            self -- instance of the class
            status -- the initial status of the game which should be a boolean( True or False).

        No variable returned from this method 
        '''
        self.status = status

        if self.status != True and self.status != False:

            raise ValueError

    def game_is_stop(self):
        '''
        Method -- game_is_stop  
            To change the game status to stop(False)

        Parameters:
            self -- instance of the class

        Return:
            the current game status
        '''
        self.status = False

    def game_is_running(self):
        '''
        Method -- game_is_stop  
            To change the game status to running(True)

        Parameters:
            self -- instance of the class

        Return:
            the current game status
        '''
        self.status = True
    
    def __eq__(self, other):
        '''
        Method -- __eq__  
            For comparsion with other object

        Parameters:
            self -- instance of the class
            other -- other object

        Return:
            return the boolean to express if it is equal or not equal to other object
        '''
        if other == True:

            return True
        else:

            return False


class LeaderBoard:
    '''
    This LeaderBoard class manages the leader board information such as player name and their scores.
    '''
    def __init__(self, player_name, score):
        '''
        Method -- __init__(constructor)  
            initialization of the LeaderBoard class. It save the parameters.

        Parameters:
            self -- instance of the class
            player_name -- player name(string)
            score = player's score (integer)

        No variable returned from this method 
        '''
        self.name = player_name
        self.score = score

        if self.score < 0:

            raise ValueError

    def name_of_player(self):
        '''
        Method -- name_of_player 
            Tp return the name of player

        Parameters:
            self -- instance of the class

        Return:
            the name of player
        '''
        return self.name

    def score_of_player(self):
        '''
        Method -- score_of_player 
            Tp return the score of player

        Parameters:
            self -- instance of the class

        Return:
            the score of player
        '''
        return self.score

    def score_update(self, new_score):
        '''
        Method -- score_of_player 
            Update the score of player

        Parameters:
            self -- instance of the class

        Return:
            Updated score of player
        '''
        self.score = new_score

        return self.score


def process_leaderboard_file( leader_txt ):
    '''
    Function -- process_leaderboard_file
        The functionality of function process_leaderboard_file is to
        sort the player from low score to high score based
        on their score.        

    Parameters:
        leader_txt -- A txt from the leaderboard_file.txt
        
    Return:
        a sorted list based on player's score
    '''
    leaderboard_list = []

    # Process the txt in leaderboard_file.txt
    for each in leader_txt:
        
        each = each.split( '\n' )
        
        for i in range(len(each)):

            if each[i] != '':

                leaderboard_list.append( each[i] )
                
    # If the original txt is empty, we can add "Leaders:" into the list
    if leaderboard_list == []:

        leaderboard_list.insert(0,'Leaders:')
        
    # If the original txt does have "Leaders:" text, we can add "Leaders:" into the list
    elif leaderboard_list[0].upper() != 'LEADERS:':

        leaderboard_list.insert(0,'Leaders:')


    leaderboard_list = sort_leaderboard_list(leaderboard_list)
        
    return leaderboard_list


def sort_leaderboard_list(leaderboard_list):
    '''
    Function -- sort_leaderboard_list
        The functionality of function sort_leaderboard_list is to
        

    Parameters:
        leaderboard_list -- A unsorted leaderboard list
        
    Return:
        a sorted list based on player's score
    '''
    # Remove the "Leader:" item in the list for covenience,
    # this will be added back at the end of this fucntion.
    leaderboard_list.pop(0)

    player_list = []
    score_list = []
 
    for x in range(len(leaderboard_list)):

        if leaderboard_list[x][1] == "0":

            # If the leaderboard has a player with score of 10, the index of player name is
            # different, we use to if condition to pick player name and score correctly.
            score_list.append("10")
            player_list.append(leaderboard_list[x][3:])

        else:

            score_list.append(leaderboard_list[x][0])
            player_list.append(leaderboard_list[x][2:]) 

    # Using selection sort to rank the player based on their score
    for i in range(len(score_list) - 1):

        min = i
        for j in range(i + 1, len(score_list)):
            if int(score_list[j]) < int(score_list[min]):
                min = j
                
        player_list[i], player_list[min] = player_list[min], player_list[i]
        score_list[i], score_list[min] = score_list[min], score_list[i]

    new_leaderboard_list = []

    # Merge the sorted score with the associated player name  
    for y in range(len(player_list)):

        new_leaderboard_item = score_list[y] + ":" + player_list[y]

        new_leaderboard_list.append(new_leaderboard_item)
        
    # As described above add "Leaders:" back to the first index of the list
    new_leaderboard_list.insert(0,"Leaders:")
        
    return new_leaderboard_list








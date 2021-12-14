'''
CS5001 Final Project

Mastermind code Game

Name: Zuocheng Wang


This a single player mastermind code game program made with python. 
First, this program randomly create a non-duplicated secret code of 4 colors which are selected from 6 different colors. 
Once player input their name, they can start the game by selecting the colored marbles which are at the bottom of the game  board to fill the blank marbles for guessing the secret codes. 
Player could remove their guess by clicking the "X" button before they hitting the check button which is submit the current guess. Once the check button is clicked, the next guess(run)
will automatically start and player cannot remove their submitted guess. If the guessed color is in the secret code with incorrect position, number of cows will plus 1. 
If both color and position are correct, number of bulls will plus 1. The number of bulls is visualize as red pegs and the number of cows is visualize as black pegs in the game board. 
The location of red and black pegs are randomly selected which means the location of pegs does not mean anything. Once a player completely get the secret code, the player won the game. 
If a player won with a better score and his score will be updated to the leaderboard on the right side of the game board which show the top 3 best players on this game.
Each player only has 10 chances to guess the correct secret code. If player cannot make it within 10 guesses, the player lose the game. 
In this program, player is able to play again when they lose the game or do not satisfy their score so far or want their name be on the leaderboard. 
a pop up window will ask player if they want to play again. If they enter "y" or "Y", a new turn will be automatically started without exiting the program.

There are three packages were used in this program which are turtle, random and time. Turtle is used to make the game board, random is used to create the random secret code
and time is used to control the game progress(time.sleep). A test suite for the functions and classes is also created to test the their functionality.

The important functions in this program are:

1. The function for counting the number of bulls and cows: This is the core function to give player hints from their previous guess(es) and determine if they get the secret code.

2. A nested recursion function start_run: This function has a nested get mouse click function inside which is to capture player's mouse click. Also, it is recursion function which allow player to 
					  start the next turn. The base case of the recursion is when player click exit or they do not enter "y" or "Y" on the pop up "play again" text input window.
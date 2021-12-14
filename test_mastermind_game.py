'''
CS5001 Final Project

Zuocheng Wang

Mastermind code Game Test Suite

The test suite include the testing functions or test class
for the following functions and class:

function 1: create_secret_code
function 2: count_bulls_and_cows
function 3: process_leaderboard_file
function 4: sort_leaderboard_list
class 1: CountSelection
class 2: CountRunNumber
class 3: IsGameRunning
class 4: LeaderBoard

'''

from mastermind_game_helper_functions import *
import unittest

def test_create_secret_code():
    '''
    Function -- test_create_secret_code()
        test the functionality of function create_secret_code()
        to test if it create 4 color codes and test if the color codes are
        from the given color list.
        
    Parameters:
        no parameters
    
    Return:
        no return
    '''
    test_pass = "PASSED"

    colors = ["red", "blue", "green", "yellow", "purple", "black"]

    random_color_list = create_secret_code()

    # check if the function create 4 color codes.
    if len(random_color_list) != 4:
        
        test_pass = "FAILED"
        
    # check if the color codes are from the given color list.
    for each in random_color_list:

        if each not in colors:

            test_pass = "FAILED"

    print(f"The result of testing create_secret_code function is: {test_pass}.")


def test_count_bulls_and_cows(secret_code, guess, expected_bulls, expected_cows):
    '''
    Function -- test_count_bulls_and_cows
        test count_bulls_and_cows function to check if it count number of
        cows and bulls correctly.
        
    Parameters:
        secret_code -- The secret code list
        guess -- The guess list
        expected_bulls -- expected number of bulls
        expected_cows -- expected number of cows
        
    Return:
        no return
    '''

    number_of_bulls, number_of_cows = count_bulls_and_cows(secret_code, guess)

    if number_of_bulls == expected_bulls and number_of_cows == expected_cows:

        outcome = "PASSED"

    else:
        outcome = "FAILED"

    print(f"count_bulls_and_cows function test is {outcome} => \n"
          f"The secret code list is:{secret_code}\n"
          f"The guess code list is:{guess}\n"
          f"number of bulls:{number_of_bulls}\t number of cows:{number_of_cows}\n"
          f"Expected number of bulls:{expected_bulls}\t Expected number of cows {expected_cows}")


def test_sort_leaderboard_list(leaderboard_list, expected_result):
    '''
    Function -- test_sort_leaderboard_list
        test the functionality of function sort_leaderboard_list
        to test if it can sort the player from low score to high score based
        on their scores.
        
    Parameters:
        leaderboard_list -- A unsorted leaderboard list
        expected_result -- Expected sorted leaderboard list
        
    Return:
        no return
    '''
    sorted_leaderboard_list = sort_leaderboard_list(leaderboard_list)

    test_result = "PASSED"

    if sorted_leaderboard_list != expected_result:

            test_result ="FAILED"

    print(f"sort_leaderboard_list function test is {test_result} => \n"
          f"The original leaderboard list is:{leaderboard_list}\n" 
          f"sort_leaderboard_list:{sorted_leaderboard_list}\n"
          f"Expected sorted list:{expected_result}")
        
          


def test_process_leaderboard_file(leader_txt, expected_result):
    '''
    Function -- test_process_leaderboard_file
        test the functionality of function process_leaderboard_file
        to test if it can create a sorted list based on the txt in leaderboard_file.txt        

    Parameters:
        leader_txt -- A txt from the leaderboard_file.txtr
        expected_result -- Expected sorted leaderboard list
        
    Return:
        no return
    '''
    processed_leaderboard_list = process_leaderboard_file(leader_txt)

    test_result = "PASSED"

    if processed_leaderboard_list != expected_result:

            test_result ="FAILED"

    print(f"process_leaderboard_file function test is {test_result} => \n"
          f"The original leaderboard text is:{leader_txt}\n" 
          f"returned leaderboard_list:{processed_leaderboard_list}\n"
          f"Expected list:{expected_result}")


class TestCountSelection(unittest.TestCase):
    '''
    This TestCountSelection class tests the method in CountSelection Class. Several test cases were created
    to test each method in CountSelection Class. 
    '''
    def test__init__(self):

        # __init__ Test case 1：Given a number of selection of 1 and a guess list with one selection,
        # it should equal to the given number of selection and the guess list
        number_of_selection = 1
        guess_list = ["red"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertEqual(selection.number_of_selection, 1)
        self.assertEqual(selection.guess_list, ["red"])
    
        # __init__ Test case 2：Given a number of selection of 4 and a guess list with 4 selection,
        # it should equal to the given number of selection and the guess list
        number_of_selection = 4
        guess_list = ["red", "blue", "green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertEqual(selection.number_of_selection, 4)
        self.assertEqual(selection.guess_list, ["red", "blue", "green", "black"])

        # __init__ Test case 3：Given a number of selection of 0 and a guess list with 0 selection,
        # it should equal to the given number of selection and the guess list
        number_of_selection = 0
        guess_list = []
        selection = CountSelection(number_of_selection, guess_list)
        self.assertEqual(selection.number_of_selection, number_of_selection)
        self.assertEqual(selection.guess_list, guess_list)

    def test_bad__init__(self):

        # Test test_bad__init__ case 1：Given a number of selection of 2 and a guess list with 2 selection,
        # it should not equal to the given number of selection and the guess list.
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertNotEqual(selection.number_of_selection, 3)
        self.assertNotEqual(selection.guess_list, ["red", "blue"])

        # Test test_bad__init__ case 2：Given a number of selection of 2 and a guess list with 2 selection,
        # it should not equal to the given number of selection and the guess list.
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertNotEqual(selection.number_of_selection, 3)
        self.assertNotEqual(selection.guess_list, []) 

    def test_number_of_selection(self):

        # test_number_of_selection Test case 1：Given a number of selection of 2.
        # it should equal to the given number of selection
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        num = selection.number_of_selection
        self.assertEqual(num, 2)

        # test_number_of_selection Test case 2：Given a number of selection of 2.
        # it should not equal to the given number of selection(bad case)
        number_of_selection = 3
        guess_list = ["green", "black","yellow"]
        selection = CountSelection(number_of_selection, guess_list)
        num = selection.number_of_selection
        self.assertNotEqual(num, 1)
        

    def test_add_selection_count(self):

        # test_add_selection_count Test case 1：Given a number of selection of 1. After add selection count.
        # it should equal to the 2
        number_of_selection = 1
        guess_list = ["red"]
        selection = CountSelection(number_of_selection, guess_list)
        number = selection.add_selection_count()
        self.assertEqual(number, 2)        

        # test_add_selection_count Test case 2：Given a number of selection of 2.
        # it should not equal to 3 (bad case)
        number_of_selection = 1
        guess_list = ["red"]
        selection = CountSelection(number_of_selection, guess_list)
        number = selection.add_selection_count()
        self.assertNotEqual(number, 3)            

    def test_append_guess(self):

        # test_append_guess Test case 1：Given a list with 2 codes. After append a new color code
        # it should equal to the given new list
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        new_list = selection.append_guess("red")
        self.assertEqual(new_list, ["green", "black", "red"])
        
        # test_append_guess Test case 2：Given a list with 2 codes. After append a new color code
        # it should not equal to the original lust (bad case)
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        new_list = selection.append_guess("red")
        self.assertNotEqual(new_list, ["green", "black"])

    def test_guess_list(self):

        # test_append_guess Test case 1：Given a list with 2 codes. 
        # it should equal to the given list
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertEqual(selection.guess_list, ["green", "black"])

        # test_append_guess Test case 1：Given a list with 2 codes. 
        # it should equal to different list (bad case)
        number_of_selection = 2
        guess_list = ["green", "black"]
        selection = CountSelection(number_of_selection, guess_list)
        self.assertNotEqual(selection.guess_list, ["black", "red", "yellow"])


class TestCountRunNumber(unittest.TestCase):
    '''
    This CountRunNumber class tests the method in CountRunNumber Class. Several test cases were created
    to test each method in CountRunNumber Class. 
    '''
    def test__init__(self):
        
        # __init__ Test case 1：Given a run number of 3
        # it should equal to 3
        run = CountRunNumber(3)
        self.assertEqual(run.run_number, 3)
        
        # __init__ Test case 2：Given a run number of 5
        # it should not equal to 3
        run = CountRunNumber(5)
        self.assertNotEqual(run.run_number, 3)       
       
    def test_bad__init__(self):

        # test_bad__init__ Test case 1：Given a run number of -3
        # it should raise value error
        with self.assertRaises(ValueError):
            run = CountRunNumber(-3)
        
    def test_number_of_run(self):

        # test_number_of_run Test case 1：Given a run number of 3
        # it should equal to 3
        run = CountRunNumber(3)
        self.assertEqual(run.number_of_run(), 3)
        
        # test_number_of_run Test case 2：Given a run number of 5
        # it should not equal to 4
        run = CountRunNumber(5)
        self.assertNotEqual(run.number_of_run(), 4)         
       

    def test_add_run_number(self):

        # test_add_run_number Test case 1：Given a run number of 3, then add run number
        # it should equal to 4
        run = CountRunNumber(3)
        run.add_run_number()
        self.assertEqual(run.number_of_run(), 4)        

    def test_reset_to_zero(self):

        # test_reset_to_zero Test case 1：Given a run number of 5, then reset to zero
        # it should equal to 0
        run = CountRunNumber(5)
        run.reset_to_zero()
        self.assertEqual(run.number_of_run(), 0)  

    def test__str__(self):

        # test__str__ Test case 1：Given a run number of 5
        # it should equal to string "5"
        run = CountRunNumber(5)
        self.assertEqual(run.__str__(), "5")


class TestIsGameRunning(unittest.TestCase):
    '''
    This TestIsGameRunning class tests the method in IsGameRunning Class. Several test cases were created
    to test each method in IsGameRunning Class. 
    '''
    def test__init__(self):
        
        # __init__ Test case 1：Given a status of True
        # it should equal to True
        is_game_run = IsGameRunning(True)
        self.assertEqual(is_game_run.status, True)
        
        # __init__ Test case 2：Given a status of False
        # it should not equal to True
        is_game_run = IsGameRunning(False)
        self.assertNotEqual(is_game_run.status, True)     


    def test_bad__init__(self):

        # test_bad__init__ Test case 1：Given a string input to the class
        # it should raise value error
        with self.assertRaises(ValueError):
            is_game_run = IsGameRunning("running")
        
    def test_game_is_stop(self):

        # test_game_is_stop Test case 1：given a boolean of True, and run game_is_stop
        # it should equal to False
        is_game_run = IsGameRunning(True)
        is_game_run.game_is_stop()
        self.assertEqual(is_game_run.status, False)        
       

    def test__eq__(self):

        # test__eq__ Test case 1：input boolean into the class to
        # create 3 objects. 1 and 2 should not equal and 1 and 2 should equal.
        is_game_run_1 = IsGameRunning(True)
        is_game_run_2 = IsGameRunning(False)
        is_game_run_3 = IsGameRunning(True)

        
        self.assertTrue(is_game_run_1.status == is_game_run_3.status)
        self.assertFalse(is_game_run_1.status == is_game_run_2.status)    


class TestLeaderBoard(unittest.TestCase):
    '''
    This TestLeaderBoard class tests the method in LeaderBoard Class. Several test cases were created
    to test each method in LeaderBoard Class. 
    '''
    def test__init__(self):
        
        # __init__ Test case 1：Input a player name and score
        leader_board = LeaderBoard("Zuocheng Wang", 6)
        self.assertEqual(leader_board.name, "Zuocheng Wang")
        self.assertEqual(leader_board.score, 6)
        
        # __init__ Test case 2：Input a player name and score
        leader_board = LeaderBoard("Zuocheng Wang", 6)
        self.assertNotEqual(leader_board.name, "Wang")
        self.assertNotEqual(leader_board.score, 10)  


    def test_bad__init__(self):

        # test_bad__init__ Test case 1：input a player name and negative score
        # it should raise value error.
        with self.assertRaises(ValueError):
            leader_board = LeaderBoard("Zuocheng Wang", -6)


    def test_name_of_player(self):

        # name_of_player Test case 1：Input a player name and score
        leader_board = LeaderBoard("Zuocheng Wang", 6)
        self.assertEqual(leader_board.name, "Zuocheng Wang")

    def score_of_player(self):

        # score_of_player Test case 1：Input a player name and score
        leader_board = LeaderBoard("Zuocheng Wang", 6)
        self.assertEqual(leader_board.score, 6)

    def score_update(self, new_score):

        # score_update Test case 1：Input a player name and score
        leader_board = LeaderBoard("Zuocheng Wang", 6)
        leader_board.score_update(2)
        self.assertEqual(leader_board.score, 2)




def main():

    # test_create_secret_code function. It should pass the test.
    test_create_secret_code()
    
    print("***********************************************")
    # test_count_bulls_and_cows function:
    # test case 1: This test case should have 0 bulls and 4 cows as all colors are correct, but position are wrong.
    secret_code= ["red", "blue", "black", "yellow"]
    guess = ["blue", "red", "yellow", "black"]
    test_count_bulls_and_cows(secret_code, guess, 0, 4)
    print("\n")
    
    # test case 2: This test case should have 4 bulls and 0 cows as all colors and locations are correct.
    secret_code= ["red", "blue", "black", "yellow"]
    guess = ["red", "blue", "black", "yellow"]
    test_count_bulls_and_cows(secret_code, guess, 4, 0)    
    print("\n")
    
    # test case 3: This test case should have 2 bulls and 2 cows as 2 colors correct and 2 colors and locations are correct.
    secret_code= ["red", "yellow", "black", "green"]
    guess = ["red", "yellow", "green", "black"]
    test_count_bulls_and_cows(secret_code, guess, 2, 2)
    print("\n")

    
    print("***********************************************")
    
    # test_sort_leaderboard_list function test case 1. It should pass the test.
    leader_board_list = ["Leaders:", "10: Zuocheng Wang", "4: Anna", "2: wzc", "5: Chris"]
    expected_list = ["Leaders:", "2: wzc", "4: Anna","5: Chris", "10: Zuocheng Wang",]
    test_sort_leaderboard_list(leader_board_list, expected_list)
    print("\n")
    
    print("***********************************************")

    # test_process_leaderboard_file function case 1. It should pass the test.
    leader_board_txt = ["10: Zuocheng Wang\n4: Anna\n2: wzc\n5: Chris"]
    expected_processed_list = ["Leaders:", "2: wzc", "4: Anna","5: Chris", "10: Zuocheng Wang",]
    test_process_leaderboard_file(leader_board_txt, expected_processed_list)    
    print("\n")
    
    # test_process_leaderboard_file function case 2. The original text has no "Leaders:".
    # It should still pass the test.
    leader_board_txt = ["10: Zuocheng Wang\n4: wzc\n5: Chris"]
    expected_processed_list = ["Leaders:", "4: wzc", "5: Chris", "10: Zuocheng Wang",]
    test_process_leaderboard_file(leader_board_txt, expected_processed_list) 
    print("\n")
    print("***********************************************")
    
    # Run the unit test in main()
    unittest.main(verbosity = 3)
main()

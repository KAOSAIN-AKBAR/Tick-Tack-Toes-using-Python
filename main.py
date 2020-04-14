
#                                                    TICK TACK TOE

# general flow of our program

# we need a board
# display the board
# function to play game
# handle a turns
# function to check win
    # check rows
    # check colomns
    # check diagonals
# function to check tie
# function to flip player

# GLOBAL VARIABLES


# first we need a board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# if the game is still going
game_still_going = True

# who won or tie ?
winner =  None

# whose turn is it ?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# lets try to start a game

def play_game():

    # first option to play the game is to display the board
    display_board()

    # loop for looping through turns X's turns and O's turns
    while game_still_going:

        # game still going, I want to handle a turn; finding out whose turn is this X's or O's turn
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # if the game is not over, we will flip to the other player
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# function to handle turn of an arbitrary player
def handle_turn(player):

    # first requires the position where the user would place their input turn
    position = input("Choose a positino from 1-9 : ")

    # type casting the input from string to integer since our board is integer type;
    # position - 1 is done since indexing of the lists starts from 0
    position = int(position)-1

    # placing the input in the on the desired position on the board
    board[position] = "X"

    # displaying the input
    display_board()


def check_if_game_over():

    # two criterias for ending the game
    check_if_win()
    check_if_tie()

def check_if_win():
    # check rows
    # check coloumns
    # check diagonals
    return

def check_if_tie():
    # check rows
    # check coloumns
    # check diagonals
    return

def flip_player(): # check players turn and give X or O this opportunity
    # flips the player x to o
    return

play_game()

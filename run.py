from random import randint

scores = {"computer": 0, "player": 0}
HIDDEN_BOARD = [[' ']*10 for x in range(10)]
GUESS_PATTERN = [[' ']*10 for x in range(10)]
letters_to_numbers={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8, 'J':9,}


def input_details():
    """
    This function allows the user/player to enter a username.
    """
  
    while True:
        print('Please enter your username.')
        print('username must not contain numbers or/and special characters')
        print('Must be no longer than 6 characters')
        print("Example: Neocal etc.....\n")

        username = input("Enter your username here:\n")
        
        if validate_username(username):
            print(f'Hello {username}, Welcome to Battleship Madness!')
            break

def validate_username(values):
    """
    Validate the username being entered. So that it is exactly:
    1. Is 6 characters long.
    2. Contains no numbers or special characters.
    """
    if len(values) > 6:
        print(f"username must be less than or equal to 6 characters long, you provided {len(values)}.")
        return False
    elif any(char.isnumeric() for char in values):
        print(f"the username {values} cannot be used, please don't use numbers.")
        return False
    elif not any(char.isalnum() for char in values):
        print(f"the username {values} cannot be used, please don't use non-alphabetic characters.")
        return False

    return True

def board_print_out(board):
    print('A B C D E F G H I J')
    print('---------------------')
    row_of_numbers = 1
    for row in board:
        print("%d|%s|" % (row_of_numbers, "|".join(row)))
        row_of_numbers += 1

def ships_creation(board):
    for ship in range(7):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,9), randint(0,9)
        board[ship_row][ship_column] == 'X'
        

def ship_location_choices():
    """
    Function that will give the computer a random choice and the Player an 
    option to provide a choice and the result of those choices.
    Computers choice,
    Players choice,
    Result of each choice.

    """
    pass


def validating_player_choice():
    """
    A function that will prevent the player from entering wrong input i.e.:
    Must be a number to signify a row and or column.
    Tray and Value Error function. 
    While loop, return True, False

    """
    pass


def end_game():
    """
    This will end the when the number of ships that are determined have been hit
    """
    pass


def new_game ():
    login_data = input_details()



new_game ()
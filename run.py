from random import randint

scores = {"computer": 0, "player": 0}


def input_details():
    
        print('Please enter your username.')
        print('username must not contain numbers or/and special characters')
        print('Must be no longer than 6 characters')
        print("Example: Neocal etc.....\n")

        username = input("Enter your username here:\n")
        validate_username(username)



def validate_username(values):
    """
    Validate the username being entered. So that it is exactly:
    1. Is 6 characters long.
    2. Contains no numbers or special characters.
    """
    try:
        if len(values) > 6:
            raise ValueError(
                f'username must be less than or equal to 6 characters long, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Inavild data: {e}, please try again.')

input_details()
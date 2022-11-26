from random import randint

scores = {"computer": 0, "player": 0}


def input_details():
    
        print('Please enter your username.')
        print('username must not contain numbers or/and special characters')
        print('Must be no longer than 6 characters')
        print("Example: Neocal etc.....\n")

        username = input("Enter your username here:\n")
        print(f"Your username is {username}")

input_details()
import random
import time

elements = ['Rock', 'Papers', 'Scissors']


def intro():
    print("""Hello,
This is a rock, papers and scissors game.
You are playing with Computer...""")
    print()
    time.sleep(1)
    print("""'R' for Rock
'P' for Papers
'S' for scissors""")


def the_game():
    points_user = 0
    points_computer = 0

    while True:
        print()
        print()
        computer = random.choice(elements)
        user_input = input("Enter Your Object: ").upper()
        if user_input == 'R' or user_input == 'P' or user_input == 'S':
            print('Thinking...')
            time.sleep(1)
            print(f'Computer: {computer}')
        else:
            pass

        if user_input == 'R':
            if computer == 'Scissors':
                points_user += 1
            elif computer == 'Papers':
                points_computer += 1
            else:
                pass

        elif user_input == 'P':
            if computer == 'Rock':
                points_user += 1
            elif computer == 'Papers':
                pass
            else:
                points_computer += 1

        elif user_input == 'S':
            if computer == 'Rock':
                points_computer += 1
            elif computer == 'Papers':
                points_user += 1
            else:
                pass

        else:
            while True:

                user_input = input("Invalid input, try again: ").upper()
                if user_input == 'R' or user_input == 'P' or user_input == 'S':
                    break
                else:
                    pass
        print()
        print(f'You :- {points_user}')
        print(f'Computer :- {points_computer}')

        if points_user == 5 or points_computer == 5:
            break
        else:
            pass
    if points_user == 5:
        print('Congrats,You Won!')
    else:
        print('Oops,You Lose!')


intro()
the_game()

time.sleep(2)

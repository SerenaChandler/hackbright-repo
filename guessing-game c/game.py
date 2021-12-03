"""A number-guessing game."""
# Put your code here

import random


def game(total_tries):
    print("Welcome to the Guessing Game")

    name = input("What's your name")
    guess = -1
    tries = 0

    num = random.randint(0,100)

    while guess != num:
        print(tries)
        guess = input(">What number would you like to guess")
        try:
            int(guess)
            it_is = True
        except ValueError:
            it_is = False
        while it_is == False:
            print("Please enter a number between 1 and 100")
            guess = input(">What number would you like to guess")
            try:
                int(guess)
                it_is = True
            except ValueError:
                it_is = False
        guess = int(guess)
        if guess > num:
            print("Too High")
        elif guess < num:
            print("Too Low")
        if tries > 9:
            print("Sorry, you lose")
        elif guess == num:
            if tries < total_tries:
                total_tries = tries + 1
        tries = tries + 1
        


    print(f"Congratulations {name}. It took you {tries} tries. High Score is {total_tries}" )
    again = input("would you like to play again? Y/N")
    if again == "Y" or again == "y":
        game(total_tries)

game(100)

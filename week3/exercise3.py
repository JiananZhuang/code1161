"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\welcome to the guessing game!")

    lowerbound = not_number_rejector("Enter a lower bound")
    upperbound = not_number_rejector("Enter a upper bound")

    while lowerbound >= upperbound:
        upperbound = not_number_rejector("Enter an upper bound higher than the lower")

    print("OK then, a number between {} and {} ?".format(lowerbound, upperbound))

    actualNumber = random.randint(lowerbound, upperbound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = int(input("guess a number: "))
            print("you guessed {},".format(guessedNumber))
            if guessedNumber > actualNumber:
                print("too big, try again   ")
            elif guessedNumber < actualNumber:
                print("too small, try again ")
            else:
                print("you got it!! It was {}".format(actualNumber))
                guessed = True
                

        except ValueError: 
            print("That's not a number, try again.")

            continue
    return ('You got it!')




if __name__ == "__main__":
    advancedGuessingGame()

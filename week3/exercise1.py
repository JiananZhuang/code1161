# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""



def loop_ranger(start, stop=10, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    a_list = []
    a = start
    while a < stop:
        a_list.append(a)
        a = a + step
    
    return a_list
  



def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    b_list = []
    b = start
    while b < stop:
        b_list.append(b)
        b = b + step

    return b_list

'''for b in range(2, 10, 1):
    print (b)'''

    


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """

    c_list = []
    c = start
    while c < stop:
        c_list.append(c)
        c = c + 2
    
    return c_list

'''for c in range(2, 10, 2):
    print (c)'''


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """

    d_list = []
    d = start
    flag = 0
    while d < stop:
        d_list.append(d)
        if flag % 2 == 0:
            d += even_step
        else:
            d += odd_step
        flag += 1
    return d_list

import random

def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """

    message = ("Enter a number between {low} and {high}: ".format(low=low, high=high))

    while True:
        guess = int(input(message))
        if low < guess < high:
            print("that number is in range!")
            return guess
        
        else:
            print("Try again!")
    


       


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    
    while True:
        try:
            a_guess = int(input(message))
            return a_guess
        except ValueError: 
            print("{} is not a number, try again.")
        except TypeError:
            print("{} is not a number, try again.")

    


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    flag = False
    message = 'Guess a number: '
    while True:
        try:
            guess = int(input(message))

            if guess < low:
                print("guess is low")
            elif guess > high:
                print("guess is high")
            else:
                print("your number is in range!")
                return guess

        except Exception as e: 
            print("{} is not a number, try again.".format(e))


    # make sure guess_n is a valid number
    '''while not flag:
        try:
            guess_number = int(input('input a nubmer between {} and {}: '.format(low,high)))
        
            if guess_number > n:
                print("Your guesses is too high, Try again")

            elif guess_number < n:
                print("Your guesses is too low, Try again")
            
            else:
                print("You Win !!!")

                flag = True
                return

        except ValueError:
            print ('Please try a number')    
        # guess_n now is a valid number 
        # find the right one
            continue'''




if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)

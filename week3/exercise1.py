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

for b in range(2, 10, 1):
    print (b)

    


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

for c in range(2, 10, 2):
    print (c)


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
        elif flag % 2 == 1:
            d += odd_step
        flag += 1
    return d_list

def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    import random
    n = random.randint(low, high)
    guess = int(input("Enter a number: "))

    if n == guess:
        print('Yes, You guessed it!')
        return

    while n != guess:
        if guess < n:
            print("guess is low")
            guess = int(input("Enter a number: "))
        elif guess > n:
            print("guess is high")
            guess = int(input("Enter a number: "))
        else:
            print("you guessed it!")
            break

       


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    a_guess = input(message)

    while type(a_guess) != int():
        print("Enter Something else")

    if type(a_guess) == int():
        print("Thank you, that is the one")

    return


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    pass

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

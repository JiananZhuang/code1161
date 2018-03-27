# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """

    testlist = range(low, high) #this give a list of testing number.
    first = testlist[0]   #the first item of the list
    last = len(testlist)-1 #the last item is the length of the list - 1
    found = False
            
    while first <= last and not found: #If the first number small and equal to last one and not found

        midpoint = (first + last) // 2 # midpoint is the first number + last number divided by 2
        if testlist[midpoint] == actual_number: # if the midpoint is the actualnumber then ture and return
            found = True
            return actual_number
        else:                           #if the actual number is smaller than the mid number, the last number = midpoint -1, and vice versa
            if actual_number < testlist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


	


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

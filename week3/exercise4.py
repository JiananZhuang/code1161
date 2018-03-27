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

1	def binarySearch(alist, high):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5	
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == high:
9	            found = True
10	        else:
11	            if high < low[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15	
16	    return found
17	
18	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19	print(binarySearch(testlist, 3))
20	print(binarySearch(testlist, 13))
    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

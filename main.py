# -*- coding: utf-8 -*-

""" Exercise 1
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Three” instead of the
number and for the multiples of five print “Five”.
For numbers which are multiples of both three and five print
“ThreeFive”.

Requirements: No dependencies needed.

To run this please do `python main.py`
To run test please do `python test.py`
"""


def is_multiple_of_x(n, x):
    """Determine if n is multiple of x."""
    return n % x == 0


def print_numbers(n):
    """Return numbers from 1 to n, doing some peculiar printings according to:

    Multiples of 3: Print "Three"
    Multiples of 5: Print "Five"
    Multiples of 3 and 5: Print "ThreeFive"

    Keywords arguments:
    n: Integer threshold

    Return an iterator which cares about the range
    """

    # List comprehension could has been tried but better readable
    # over idiomatic, also n could be bigger than 100 so better return an
    # iterator
    for i in xrange(1, n + 1):
        result = ''
        if is_multiple_of_x(i, 3):
            result += 'Three'
        if is_multiple_of_x(i, 5):
            result += 'Five'
        if not result:
            result = str(i)
        yield result


if __name__ == "__main__":
    n = 100
    for i in print_numbers(n):
        print i

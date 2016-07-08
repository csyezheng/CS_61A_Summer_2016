# 1. (5 points) Print If
#    Implement the print_if function, which takes a non-negative integer n and a predicate function pred.1
#    print_if prints out all non-negative integers from 0 to n-1 (inclusive) for which pred returns True, in
#    increasing order, and returns the number of integers that it printed.

def is_even (x):
    return x % 2 == 0
def is_greater_than_three (x):
    return x > 3
def print_if (n, pred ):
    """
    >>> # 0, 2, 4, 6 are the non - negative even integers less than 8.
    >>> even_count = print_if (8, is_even )
    0
    2
    4
    6
    >>> even_count
    4
    >>> # 4, 5 are greater than 3 and less than 6.
    >>> range_count = print_if (6, is_greater_than_three )
    4
    5
    >>> range_count
    2
    """
    times = 0
    curr = 0
    while curr < n:
        if pred(curr):
            print(curr)
            times += 1
    return times

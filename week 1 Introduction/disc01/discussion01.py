# 1.3 Questions

# 1. Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining. Fill 
#    in the function wears jacket which takes in the current temperature and a Boolean
#    value telling if it is raining and returns True if Alfonso will wear a jacket and False
#    otherwise.

def wears_jacket(temp, raining):
    """
    >>> rain = False
    >>> wears_jacket(90, rain)
    False
    >>> wears_jacket(40, rain)
    True
    >>> wears_jacket(100, True)
    True
    """
    return raining or (temp < 60)


# 2. To handle discussion section overflow, TAs may direct students to a more empty section
#    that is happening at the same time. Write the function handle overflow, which
#    takes in the number of students at two sections and prints out what to do if either section
#    exceeds 30 students. See the doctests below for the behavior.

def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow.
    >>> handle_overflow(35, 29)
    1 spot left in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section.
    """
    if s1 <= 30 and s2 <= 30:
        print("No overflow.")
    elif s2 > 30 and s1 < 30:
        print(str(30 - s1) + "spots left in Section 1.")
    elif s1 > 30 and s2 < 30:
        print(str(30 - s2) + "spots left in Section 2.")
    else:
        print("No space left in either section.")


# 1.5 Questions

# 1. What is the result of evaluating the following code?

def square(x):
    return x * x
def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
square(so_slow(5))      # Error


# 2. Fill in the is prime function, which returns True if n is a prime number and False
#    otherwise. After you have a working solution, think about potential ways to make
#    your solution more efficient.
#    Hint: use the % operator: x % y returns the remainder of x when divided by y.
def is_prime(n):
    """ To test the parameter is prime or not
    
    >>> is_prime(1)
    >>> False
    >>> is_prime(2)
    >>> True
    """
    def square(x):
        return x * x
    assert type(n) == int, 'not an integer'
    assert n > 0, 'this number should greater than 0'
    if n == 1:
        return True
    curr = 2
    while square(curr) < n:
        if n % k == 0:
            return False
        curr += 1
    return True


# 1.6 Have Some More Control!

# 1. Implement fizzbuzz(n), which prints numbers from 1 to n (inclusive). However,
#    for numbers divisible by 3, print “fizz”. For numbers divisible by 5, print “buzz”. For
#    numbers divisible by both 3 and 5, print “fizzbuzz”.

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    assert type(n) == int, 'the parameter must be an integer.'
    assert n > 0, 'the number must be greater than 0'
    curr = 1
    while curr <= n:
        if curr % 3 == 0:
            if curr % 5 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        elif curr % 5 == 0:
            print('buzz')
        else:
            print(curr)
        curr += 1


# 2.3 Questions

# 1. What would Python print?

>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])               # 1, 3
>>> len(a)                           # 5
>>> 2 in a                           # False
>>> 4 in a                           # True
>>> a[3][0]                          # 2

# 2. What would Python print?

>>> apple = [3, 2, 1, 0]
>>> def banana(fruits):
        for apple in fruits:
            print(apple)
>>> banana(apple)

# 3
# 2
# 1
# 0

# 3. What would Python print?

>>> x = [1, 3, 5, 7]
>>> def partial(lst):
        first = lst[0]
        if first == 3:
            print('Hello')
        else:
            print('Goodbye')
        return lst
>>> partial(x)

# Goodbye
# 1, 3, 5, 7

# 4. What would Python print?

>>> lst = [3, 2, 1, 0]
>>> def fungus(spore):
        x = 0
        while spore[x] != 0:
            print('Mushroom!')
            x += 1
        return x
>>> fungus(lst)

# Mushroom!
# Mushroom!
# Mushroom
# 3

# 5. Define a function print negative that takes in a list lst and prints all the negative
#    numbers in the list.

def print_negative(lst):
    for value in lst:
        if value < 0:
            print(value)

# 3.1 Environment Diagram Questions

# 1. Draw the environment diagram that results from running the following code.

a = 1
def b(b):
    return a + b
a = b(a)
a = b(a)



# 2. Draw the environment diagram so we can visualize exactly how Python evaluates the
#    code. What is the output of running this code in the interpreter?

>>> from operator import add
>>> def sub(a, b):
    ... sub = add
    ... return a - b
>>> add = sub
>>> sub = min
>>> print(add(2, sub(2, 3)))

# 0

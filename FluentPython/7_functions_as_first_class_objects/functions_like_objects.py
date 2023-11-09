# In Python functions are first-class objects. This concept means that functions can be treated similarly to any other data type.
# They can be created at runtime, assigned to a variable or element in a data structure, passed as an argument to a function or returne as a result of a function

def factorial(n):
    """Returns n!"""

    return 1 if n < 2 else n * factorial(n-1)

print(factorial(5)) # 120
print(type(factorial)) # <class 'function'>

fact = factorial # function assigned to a variable

# Pass a function as a parameter
import random

def age_random():
    return random.randint(0,99)

def say_hello(rand):
    return f"Hello, Andrea's here. I'm {rand()}"

print(say_hello(age_random)) # Hello, Andrea's here. I'm <random_number>

# Make an iterator that computes the function using arguments from each of the iterables.
results = list(map(factorial, range(10)))
print(results) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# Map e filter are first-class objetcs built-in in Python 3 but since the introduction of list comprehensions they are not as important.
# List comprehensions do the same job but they are more readable.

l = [factorial(n) for n in range(10)]
print(l) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# map e filter used together. List comprehension is more readble
l = list(map(factorial, filter(lambda n: n % 2, range(10))))
print(l) # [1, 6, 120, 5040, 362880]

l = [factorial(n) for n in range(10) if n % 2] 
print(l) # [1, 6, 120, 5040, 362880]

l = [2,4,5]
even_number_presence = any(n % 2 == 0 for n in l)
print(even_number_presence) # True

all_numbers_even = all(n % 2 == 0 for n in l)
print(all_numbers_even) # False
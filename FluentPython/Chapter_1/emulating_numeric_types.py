"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.

This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v) -> (x^2+y^2)^(1/2)
    5.0

Scalar multiplication::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

"""

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Unambiguous print
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
    
    # Human readable print
    def __str__(self):
        return f"v({self.x},{self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)

v1 = Vector(1, 4)
v2 = Vector(3, 5)
print(v1)

v3 = v1 + v2
print(v3)

v4 = v1 * 2
print(v4)

print(abs(v1))

v5 = Vector(0,0)

if(v5):
    print("Vector's magnitude is greater than zero")
else:
    print("Vector magnitude is zero")
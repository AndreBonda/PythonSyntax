from typing import Any

# The keystone of any gradual type system is the Any type

# when type checker sees this function, it assumes def double(x: Any) -> Any


def double(x):
    return x * 2

# Any type is 'consistent-with' other types.
# - you can pass objects to every type to an argument declared of type Any
# - you can pass an object of type Any to an argument of another type

class T1:
    pass

class T2(T1):
    pass

def f3(p: Any) -> None:
    pass

o0 = object()
o1 = T1()
o2 = T2()

f3(o0) # ok
f3(o1) # ok
f3(o2) # ok

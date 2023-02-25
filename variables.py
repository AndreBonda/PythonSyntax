# Variables are dynamicly typed
n = 0
print('n =', n)

n = "abc"
print('\nn =', n)

# Multiples assignments
n, m = 0, "abc"
print('\nn =', n)
print('m =', m)

# Increment
n = 1
n = n+1
n += 1
print('\nn =', n)

# None is null
n = None
print('\nn =',n)

# If statements don't need parentheses or curly braces
n = -2
if n > 0:
    print('Inside if')
elif n == -1:
    print("Inside elif")
else:
    print('Inside else')
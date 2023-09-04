# modi per inizializzare un set

# using curly braces
basket = {'mele', 'pere', 'banane'}

# using set constructor for empty set
mySet = set()

# using set constructor from a list
mySet = set([1,1,2,3]) # second '1' is ignored

# using list comprehension
mySet = {i for i in range(5)}
print(mySet) # 0 1 2 3 4

letters = [x for x in "abracadabra" if x not in "abc"]
print(letters) # ['r', 'd', 'r']

# Remove and return an arbitrary set element
mySet = set([1,5,3,9,4,15,13])
print("----- Pop")
print(mySet.pop())

# check element presence
s = {1,2,3}
print(2 in s) # True

# differences
a = {1,2,3,4}
b = {2,4,5}
print(a-b) # 1,3
print(a | b) # {1, 2, 3, 4, 5} union of elements
print(a & b) # {2, 4} elements in both sets
print(a ^ b) # {1,3,5} elements in a or b but not both
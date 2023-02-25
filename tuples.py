# Tuples are like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

# Can be used as key for hash map/set
myMap = {(1,2): 3}
myMap = {(3,4): 3}
print(myMap)
print((3,4) in myMap) # True
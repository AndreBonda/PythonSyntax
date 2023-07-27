# empty dictionary
d = {}

# inizializzazione inline
d = {"alice": 90, "bob": 100}

# add key-value pair
d["max"] = 88

# delete key-value pair
del d["bob"]
print(d)

# listing of keys
print(list(d)) # ['alice', 'max]

# presence
print("alice" in d) # True
print("alice" not in d) # False

# use dict constructor to build dictionaries from a list of key-value pairs
d = dict([("Andrea", 28), ("Marco", 30)])
print(d)

# dict comprehension
d = {x: x**2 for x in range(5)}
print(d)

word = "abcdef"
letters = {index: value for index, value in enumerate(word)}
print(letters)

# looping through maps
print('\n')
myMap = {"alice": 90, "bob": 100, "beth": 45}
for key in myMap:
    print(key, myMap[key])

# iterate for values
for val in myMap.values():
    print(val)

# iterate for items
for key, val in myMap.items():
    print(key, val)

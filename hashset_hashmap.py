mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(2) # ignored

print(mySet)

# list to set
mySet = set([1,2,3,4])
print(mySet)

# set comprehension
mySet = {i for i in range(5)}
print(mySet) #01234

myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(myMap["alice"])

# inizializzazione inline
myMap = {"alice": 90, "bob": 100}
print(myMap)

myMap = {i: i*2 for i in range(3)} # map --> 0,0 - 1,2 - 2,4
print(myMap)

# looping through maps
print('\n')
myMap = {"alice": 90, "bob": 100, "beth": 45}
for key in myMap:
    print(key, myMap[key])

# iterate for values
print()
for val in myMap.values():
    print(val)

# iterate for items
print()
for key, val in myMap.items():
    print(key, val)
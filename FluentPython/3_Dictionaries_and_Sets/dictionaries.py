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
d = dict([("Andrea", 28), ("Marco", 30)]) # {'Andrea': 28, 'Marco': 30}
print(d)

# looping through maps
print('\n')
myMap = {"alice": 90, "bob": 100, "beth": 45}
for key in myMap:
    print(key, myMap[key])

# .keys(), .values(), .items() ritornano rispettivamente istanze delle classi dict_keys, dict_values, dict_items, ovvero delle proiezioni readonly della struttura dati usata internamente per l'implementazione dei dictionaries.

keys = myMap.keys()
print(keys) # dict_keys(['alice', 'bob', 'beth'])

# iterate for values
values = myMap.values()
print(values) # dict_values([90, 100, 45])

# iterate for items
items = myMap.items() # dict_items([('alice', 90), ('bob', 100), ('beth', 45)])
print(items)

# Non è possibile modificare una view
# values[0] = 150 # TypeError: 'dict_values' object does not support item assignment

# Le view sono proiezioni dinamiche
myMap['alice'] = 999
print(values) # dict_values([999, 100, 45])
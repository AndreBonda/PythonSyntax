# Strings are similar to arrays
s = "abc"
print(s[0:2]) # ab

# le stringhe sono immutabili
# la modifica di una string consiste nella creazione di una nuova
s += "def"
print(s)

# convert strings into numbers
print(int("123") + int("123")) # 246

# convert numbers into strings
print(str(123) + str(123)) # 123123

# get ASCII value of a character
print(ord('A')) # 65

# combine a list of strings (with an empty strings delimitor)
strings = ["ab", "cd", "ef"]
print("-".join(strings))
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

# Array to string
print("--- Array to string ---")
strings = ["ab", "cd", "ef"]
print("-".join(strings)) #combine a list of strings (with an empty strings delimitor)

chars = ["a","n","d","r","e","a"]
print("".join(chars)) # andrea

print("pad left")
string = "ciao_mare"
padded = string.rjust(20, '0')
print(padded) 

print("integer to bin")
i = 3
print("", i, " in binario: ", bin(i))

# Get only alphanum from a string
print("--- Get only alphanum characters from a string ---")
string = "Abc _!12"
chars = [c for c in string if c.isalnum()]
print(chars) # Abc12
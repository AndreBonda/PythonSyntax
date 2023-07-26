# Strings are similar to arrays
s = "abc"
print(s[0:2]) # ab

# le stringhe sono immutabili
# la modifica di una string consiste nella creazione di una nuova
s += "def"
print(s)

# essendo immutabili è possibile accedere in lettura ad un carattere
# in base alla posizione ma non è possibile modificarlo
s = "hello"
print(s[1]) # -> e
# s[0] = 'z' -> errore a runtime

# convert strings into numbers
print(int("123") + int("123")) # 246

# convert numbers into strings
print(str(123) + str(123)) # 123123

# get ASCII value of a character
print(ord('A')) # 65

# Array to string
print("--- Array to string ---")
strings = ["ab", "cd", "ef"]
#combine a list of strings (with an empty strings delimitor)
print("-".join(strings)) # -> ab-cd-ef

chars = ["a","n","d","r","e","a"]
print("".join(chars)) # andrea

print("pad left")
string = "ciao_mare"
padded = string.rjust(20, '0')
print(padded) # -> 00000000000ciao_mare

print("integer to bin")
i = 3
print("", i, " in binario: ", bin(i))

# Get only alphanum from a string
print("--- Get only alphanum characters from a string ---")
string = "Abc _!12"
chars = [c for c in string if c.isalnum()]
print(chars) # Abc12

# Split string removing white spaces (anche spazi multipli)
string = "Ciao  mi  chiamo   Andrea"
no_empty_words = [word for word in string.split(" ") if word]
print(no_empty_words)

# raw string
raw = r"C:\some\name" # -> C:\some\name
print(raw)

multi_line = """
ciao,
mare"""
print(multi_line)

# String concat
concat = 'a' * 3 + 'b'
print(concat) # -> aaab